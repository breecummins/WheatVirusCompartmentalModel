import SImodel as sim
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

initial_condition = 0.50
numsteps = 1000

Cvals = list(range(5,45,5))
WVvals = list(range(10,101,10))
Wvals = list(range(250,251,20))

# X,Y,Z = np.meshgrid(Cvals,WVvals,Wvals)
# (a,b,c) = X.shape

param_grid = np.zeros((3, len(Cvals), len(WVvals), len(Wvals)))

for h,climate in enumerate(["am","ot","ro"]):
    for i,C in enumerate(Cvals):
        for j,WV in enumerate(WVvals):
            for k,W in enumerate(Wvals):
                param_grid[h,i,j,k] = sim.oneyear([C,WV,W,WV],climate,initial_condition,numsteps)[0]

X, Y = np.meshgrid(Cvals,WVvals)

fig = plt.figure()
ax = fig.gca(projection='3d')

# print(X.transpose())
# print(Y.transpose())
Z = np.squeeze(param_grid[:1,:,:,:1])
# print(Z)
ax.plot_surface(X.transpose(), Y.transpose(), Z)
ax.set_xlabel("cheatgrass plants per m^2")
ax.set_ylabel("volunter wheat per m^2")
ax.set_zlabel("wheat yield")
plt.title("ambient")
plt.savefig("grid_results_IC50_ambient.pdf")
# plt.show()

fig = plt.figure()
ax = fig.gca(projection='3d')

# print(X.transpose())
# print(Y.transpose())
Z = np.squeeze(param_grid[1:2,:,:,:1])
# print(Z)
ax.plot_surface(X.transpose(), Y.transpose(), Z)
ax.set_xlabel("cheatgrass plants per m^2")
ax.set_ylabel("volunter wheat per m^2")
ax.set_zlabel("wheat yield")
plt.title("hot")
plt.savefig("grid_results_IC50_hot.pdf")
# plt.show()

fig = plt.figure()
ax = fig.gca(projection='3d')

# print(X.transpose())
# print(Y.transpose())
Z = np.squeeze(param_grid[2:,:,:,:1])
# print(Z)
ax.plot_surface(X.transpose(), Y.transpose(), Z)
ax.set_xlabel("cheatgrass plants per m^2")
ax.set_ylabel("volunter wheat per m^2")
ax.set_zlabel("wheat yield")
plt.title("hot/dry")
plt.savefig("grid_results_IC50_hotdry.pdf")
# plt.show()