import numpy as np
import pandas as pd
from importlib.resources import files
import patsy as ps
import mn2 as mm
import torch as th

data = pd.read_csv(files('mn2.data').joinpath('evt12.csv').open())

data.head()

trial = data[data['site'] == 507]
trial.describe()

y = trial['yield'].to_numpy()
X = np.asarray(ps.dmatrix('~ C(variety)', trial))

RE = mm.Random([mm.VC(trial['site']), mm.VC(trial['rep'])])

t = RE.x0()

model = mm.LMM(y, X, RE)

theta0 = th.ones(1, dtype=th.double)

model.forward(theta0)

theta0[0] = 1.467167

model.forward(theta0)
