import numpy as np
import pandas as pd
from importlib.resources import files
import patsy as ps
import mn2 as mm
import torch as th

data = pd.read_csv(files('mn2.data').joinpath('oats.csv').open())
data.head()

y = data['yield'].to_numpy()
X = np.asarray(ps.dmatrix('~ C(variety)*C(nitro)', data))
interaction = data['replication'].astype(str) + ':' + data['variety'].astype(str)
RE = mm.Random([mm.VC(data['replication']), mm.VC(interaction)])

model = mm.LMM(y, X, RE)
out = model.fit()
out
