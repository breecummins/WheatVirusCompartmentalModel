import SImodel as sim
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
rc('text',usetex=True)
fontsize=16
rc('axes', labelsize=fontsize)    # fontsize of the x and y labels
rc('xtick', labelsize=fontsize)    # fontsize of the tick labels
rc('ytick', labelsize=fontsize)    # fontsize of the tick labels
rc('legend', fontsize=16)    # legend fontsize

from mpl_toolkits.mplot3d import Axes3D

initial_condition = 0.1
numsteps = 1000

Cvals = list(range(25,200,25))
WVvals = list(range(10,101,10))
Wvals = list(range(250,251,20))

param_grid = np.zeros((3, len(Cvals), len(WVvals), len(Wvals)))

for h,climate in enumerate(["am","ot","ro"]):
    for i,C in enumerate(Cvals):
        for j,WV in enumerate(WVvals):
            for k,W in enumerate(Wvals):
                param_grid[h,i,j,k] = sim.oneyear([C,WV,W,WV],climate,initial_condition,numsteps)[0]

X, Y = np.meshgrid(Cvals,WVvals)

fig = plt.figure()
ax = fig.gca(projection='3d')
zlim=[0.0,1.28]

# print(X.transpose())
# print(Y.transpose())
Z3 = np.squeeze(param_grid[2:,:,:,:1])
ax.plot_surface(X.transpose(), Y.transpose(), Z3,label="hot/dry",color="firebrick",zorder=0)
p3 = plt.Rectangle((0, 0), 1, 1, fc="firebrick")
ax.set_xlabel(r"cheatgrass plants per $m^2$")
ax.set_ylabel(r"volunter wheat per $m^2$")
ax.set_zlabel("wheat yield")
ax.set_zlim(zlim)
# plt.title("hot/dry")
# plt.savefig("grid_results_IC50_hotdry.pdf")


# print(X.transpose())
# print(Y.transpose())
Z1 = np.squeeze(param_grid[:1,:,:,:1])
# print(Z)
ax.plot_surface(X.transpose(), Y.transpose(), Z1,label="ambient",color="darksalmon",zorder=2)
p1 = plt.Rectangle((0, 0), 1, 1, fc="darksalmon")
# ax.set_xlabel("cheatgrass plants per m^2")
# ax.set_ylabel("volunter wheat per m^2")
# ax.set_zlabel("wheat yield")
# ax.set_zlim(zlim)
# plt.title("ambient")
# plt.savefig("grid_results_IC50_ambient.pdf")
# plt.show()

# fig = plt.figure()
# ax = fig.gca(projection='3d')

# print(X.transpose())
# print(Y.transpose())
Z2 = np.squeeze(param_grid[1:2,:,:,:1])
# print(Z)
ax.plot_surface(X.transpose(), Y.transpose(), Z2,label="hot",color="red",zorder=3)
p2 = plt.Rectangle((0, 0), 1, 1, fc="red")
# ax.set_xlabel("cheatgrass plants per m^2")
# ax.set_ylabel("volunter wheat per m^2")
# ax.set_zlabel("wheat yield")
# ax.set_zlim(zlim)
# plt.title("hot")
# plt.savefig("grid_results_IC50_hot.pdf")
# plt.show()

# fig = plt.figure()
# ax = fig.gca(projection='3d')


ax.legend([p1,p2,p3],['ambient','hot','hot/dry'])
plt.savefig("grid_results_IC_10.pdf")
plt.show()