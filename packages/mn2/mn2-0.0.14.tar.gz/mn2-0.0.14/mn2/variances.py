import numpy as np
import pandas as pd
import torch as th

from mn2.structures import Structure, VC, AR1, CS

class Random(th.nn.ModuleList):

    def __init__(self, *args):        
        super().__init__(*args)
        
        self.indices = [ term.getr() for term in self ]
        self.slices = [ term.getq() for term in self ]

    def forward(self, theta: th.tensor):
        
        thetas = th.split(theta, self.indices)        
        blocks = [ term.forward(param) for term,param in zip(self, thetas) ]

        ZLambda = th.cat(blocks, dim=1)
        
        return ZLambda

    def getr(self): return sum(self.indices)
    def getq(self): return sum(self.slices)
    def getrs(self): return self.indices
    def getqs(self): return self.slices

    def x0(self):

        x0s = [ term.x0() for term in self ]

        return np.hstack(x0s)

