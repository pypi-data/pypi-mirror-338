import numpy as np
import pandas as pd
import torch as th

class Structure(th.nn.Module):

    def __init__(self, r: int, q: int):
        super().__init__()

        self.r = r
        self.q = q
        self.n = self.q
        self.Z = th.eye(self.q, dtype=th.double)

        self.lb = np.array([0.0])
        self.ub = np.array([np.inf])

    def __init__(self, r: int, column):
        super().__init__()

        self.r = r
        self.Z = self.setZ(column)
        self.q = self.Z.shape[1]
        self.n = self.Z.shape[0]

        self.lb = np.array([0.0])
        self.ub = np.array([np.inf])
        
    def getr(self): return self.r
    def getq(self): return self.q
    def getn(self): return self.n
    def getZ(self): return self.Z
    def getBounds(self): return np.column_stack((self.lb, self.ub))

    def setZ(self, column):

        data = pd.get_dummies(column, dtype=float, sparse=True)
        design = th.tensor(th.from_numpy(data.values).float(), dtype=th.double)

        return design

    def x0(self): return np.array([1.0])

class VC(Structure):

    def __init__(self, q: int):
        super().__init__(1, q)

        self.lb = np.array([0.0])
        self.ub = np.array([np.inf])

    def __init__(self, column):
        super().__init__(1, column)

        self.lb = np.array([0.0])
        self.ub = np.array([np.inf])
        
    def forward(self, theta: th.tensor):

        if theta.shape[0] == self.r:
            
            Lambda = th.eye(self.q, dtype=th.double) / theta[0]
            
            return self.Z @ Lambda

    def x0(self): return np.array([1.0])

class AR1(Structure):

    def __init__(self, q: int):
        super().__init__(2, q)

        self.lb = np.array([0.0, -1.0])
        self.ub = np.array([np.inf, +1.0])

    def __init__(self, column):
        super().__init__(2, column)

        self.lb = np.array([0.0, -np.inf])
        self.ub = np.array([np.inf, np.inf])
            
    def forward(self, theta: th.tensor):

        if theta.shape[0] == self.r:

            I = th.eye(self.q, dtype=th.double)
            S = th.diag(th.ones(self.q - 1, dtype=th.double), diagonal=-1)
            Lambda = (I - theta[1] * S) / theta[0]

            return self.Z @ Lambda

    def x0(self): return np.array([1.0, 0.0])

class CS(Structure):

    def __init__(self, q: int):
        super().__init__(2, q)

        self.lb = np.array([0.0, -np.inf])
        self.ub = np.array([np.inf, +1.0])

    def __init__(self, column):
        super().__init__(2, column)

        self.lb = np.array([0.0, -1.0])
        self.ub = np.array([np.inf, +1.0])
            
    def forward(self, theta: th.tensor):

        if theta.shape[0] == self.r:
            
            c1 = 1 / (theta[0] * th.sqrt(theta[1]))
            c2 = 1 / (theta[0] * th.sqrt(1 - theta[1]))
            
            dij = c2 * th.ones(self.q, dtype=th.double)
            dij[0] = c1
            D = th.diag(dij)
            
            u = th.zeros(self.q, dtype=th.double)
            u[1:] = 1.0
            
            v = th.zeros(self.q, dtype=th.double)
            v[0] = -th.sqrt(theta[1]) / c2

            Lambda = D + th.outer(u, v)

            return self.Z @ Lambda

    def x0(self): return np.array([1.0, 0.0])
