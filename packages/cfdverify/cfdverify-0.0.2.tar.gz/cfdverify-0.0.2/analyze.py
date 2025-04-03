# %%
## Import modules
import pandas as pd
from cfdverify.discretization import *

# %%
## Load data
data = pd.read_csv("Mesh_data.csv")
data2 = pd.read_csv("meshReduced.csv")

classic = Classic(data, data.keys()[0])
classic2 = Classic(data2, data.keys()[0])

# %%
#multi = CustomDiscretizationError(data, data.keys()[0], model=FirstAndSecondOrder)
# %%
classic.u(data.keys()[1], 0)