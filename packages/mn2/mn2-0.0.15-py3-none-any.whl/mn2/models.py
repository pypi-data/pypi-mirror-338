import numpy as np
import torch as th
import scipy.optimize as op

from mn2.structures import Structure, VC, AR1, CS
from mn2.variances import Random

class LMM(th.nn.Module):

    def __init__(self, response: np.array, fixed: np.array, random: Random):
        super().__init__()

        self.y = th.nn.Parameter(th.from_numpy(response).float(), requires_grad=True)
        self.n = self.y.shape[0]
        
        self.X = th.nn.Parameter(th.from_numpy(fixed), requires_grad=True)
        self.p = self.X.shape[1]
        
        self.RE = random
        self.t = self.RE.getr() # length of theta (r within structures)
        self.q = self.RE.getq()

        self.df = th.tensor(self.n - self.p, requires_grad=False)
        self.kappa = th.nn.Parameter(th.tensor(self.df * (1 + th.log(2 * th.pi / self.df))), requires_grad=True)
        
        self.ypy = th.nn.Parameter(self.y.t() @ self.y, requires_grad=True)

        ## Bates et al., 2015 Equation 16, page 14
        self.o = th.nn.Parameter(th.zeros(self.q, dtype=th.double), requires_grad=True)
        self.O = th.nn.Parameter(th.zeros([self.q, self.p], dtype=th.double), requires_grad=True)
        self.I = th.nn.Parameter(th.eye(self.q, dtype=th.double), requires_grad=True)
        self.v = th.nn.Parameter(th.hstack((self.y, self.o)), requires_grad=True)

        ## indices
        self.qis = th.linspace(0, self.q - 1, steps=self.q, dtype=th.long, requires_grad=False)
        self.pis = th.linspace(self.q, self.q + self.p - 1, steps=self.p, dtype=th.long, requires_grad=False)

    ## callable
    def __call__(self, theta):

        x = th.tensor(th.from_numpy(theta), dtype=th.double, requires_grad=True)
        f = self.forward(x)
        f.backward()

        fx = f.item()
        dx = x.grad.numpy()
        
        return fx, dx

    def forward(self, theta):

        ## mixed model equations
        ZLambda = self.RE.forward(theta)
        M = th.vstack((th.hstack((ZLambda, self.X)), th.hstack((self.I, self.O))))
        r = M.t() @ self.v
        C = M.t() @ M

        ## model's sums of squares and criteria
        e = self.solve(C, r, system=4)
        reml = self.df * th.log(self.ypy - e.t() @ e) + th.log(th.det(C)) + self.kappa

        return reml

    ## cholmod notation flag
    def solve(self, A, b, system: int=0):

        if (system == 0):
            solution = th.linalg.solve(A, b)

        if (system == 4):
            S = th.linalg.cholesky(A)
            solution = th.linalg.solve(S, b)

        return solution

    def fit(self):

        optimum = op.minimize(
            self.__call__,
            self.RE.x0(),
            method='L-BFGS-B',
            jac=True,
            options={
                'disp': True
            })
        
        ## mme
        theta = th.tensor(th.from_numpy(optimum.x).float(), dtype=th.double, requires_grad=True)
        ZLambda = self.RE.forward(theta)
        M = th.vstack((th.hstack((ZLambda, self.X)), th.hstack((self.I, self.O))))
        r = M.t() @ self.v
        C = M.t() @ M

        ## solutions
        s = self.solve(C, r, system=0)
        gamma = th.index_select(s, dim=0, index=self.qis)
        beta = th.index_select(s, dim=0, index=self.pis)

        ## estimations
        fitted = self.X @ beta + ZLambda @ gamma
        epsilon = self.y - fitted

        ## residual standard error
        rss = epsilon.t() @ epsilon
        penalty = gamma.t() @ gamma
        pwrss = rss + penalty
        sigma = th.sqrt(pwrss / self.df)

        return {
            'message': optimum.message,
            'reml': optimum.fun,
            'sigma': sigma.item(),
            'beta': beta.detach().numpy(),
            'gamma': gamma.detach().numpy(),
            'fitted': fitted.detach().numpy(),
            'residuals': epsilon.detach().numpy()
        }
