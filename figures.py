import SImodel as sim
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
rc('text',usetex=True)
fontsize=16
rc('axes', labelsize=fontsize)    # fontsize of the x and y labels
rc('xtick', labelsize=14)    # fontsize of the tick labels
rc('ytick', labelsize=14)    # fontsize of the tick labels
rc('legend', fontsize=fontsize)    # legend fontsize

from mpl_toolkits.mplot3d import Axes3D, proj3d

def simulate(Cvals,WVvals,Wvals,initial_condition):
    numsteps = 1000
    param_grid = np.zeros((3, len(Cvals), len(WVvals), len(Wvals)))

    for h, climate in enumerate(["am", "ot", "ro"]):
        for i, C in enumerate(Cvals):
            for j, WV in enumerate(WVvals):
                for k, W in enumerate(Wvals):
                    param_grid[h, i, j, k] = sim.oneyear([C, WV, W, WV], climate, initial_condition, numsteps)[0]
    return param_grid


def simulate_for_fixed_pops(deltas,C=50,WV=50,W=225,IC=0.5):
    numsteps = 1000
    results = {"ambient" : [], "hot" : [], "hot/dry" : []}
    for h, climate in enumerate(["am", "ot", "ro"]):
        for d in deltas:
            lab = "ambient" if climate=="am" else "hot" if climate=="ot" else "hot/dry"
            results[lab].append(sim.oneyear([C, WV, W, WV], climate, IC, numsteps,(d,d+0.15))[0])
    return results


def params_lowcheatgrass():
    Cvals = list(range(10, 111, 10))
    WVvals = list(range(5, 101, 5))
    Wvals = list(range(250, 251, 20))
    zord = {"ambient" : 4, "hot" : 5, "hot/dry" : 3}
    return Cvals,WVvals,Wvals,zord

def params_highcheatgrass():
    Cvals = list(range(100, 301, 25))
    WVvals = list(range(5, 101, 5))
    Wvals = list(range(250, 251, 20))
    zord = {"ambient" : 3, "hot" : 5, "hot/dry" : 4}
    return Cvals,WVvals,Wvals,zord

def plot_deltas(results,deltas):
    losses = [1-d for d in deltas]
    losses.reverse()
    plt.figure()
    for lab,data in results.items():
        data.reverse()
        plt.plot(losses,data,label=lab,linewidth=2)
    plt.xlabel(r"$1-\delta_1$",fontsize=20)
    plt.ylabel("relative wheat yield")
    plt.legend()
    plt.savefig("deltas.pdf",bbox_inches="tight")


def make_plot_no_W(Cvals,WVvals,param_grid,zord,savename,init_cond,pt):
    X, Y = np.meshgrid(Cvals,WVvals)

    fig = plt.figure()
    ax = fig.gca(projection='3d')
    zlim=[0.0,1.35]

    Z3 = np.squeeze(param_grid[2:,:,:,:1])
    ax.plot_surface(X.transpose(), Y.transpose(), Z3,label="hot/dry",color="firebrick",zorder=zord["hot/dry"])
    p3 = plt.Rectangle((0, 0), 1, 1, fc="firebrick")


    Z1 = np.squeeze(param_grid[:1,:,:,:1])
    ax.plot_surface(X.transpose(), Y.transpose(), Z1,label="ambient",color="darksalmon",zorder=zord["ambient"])
    p1 = plt.Rectangle((0, 0), 1, 1, fc="darksalmon")

    Z2 = np.squeeze(param_grid[1:2,:,:,:1])
    ax.plot_surface(X.transpose(), Y.transpose(), Z2,label="hot",color="red",zorder=zord["hot"])
    p2 = plt.Rectangle((0, 0), 1, 1, fc="red")

    f = lambda x,y,z: proj3d.proj_transform(x,y,z, ax.get_proj())[:2]
    ax.legend([p1,p2,p3],['ambient','hot','hot/dry'],loc="lower left", bbox_to_anchor=f(*pt),
              bbox_transform=ax.transData)
    ax.set_xlabel(r"cheatgrass plants per $m^2$")
    ax.set_ylabel(r"volunteer wheat per $m^2$")
    ax.set_zlabel("relative wheat yield")
    ax.set_zlim(zlim)
    plt.savefig(savename+"_{:0.2f}".format(init_cond).replace(".","_")+".pdf")
    plt.show()


def runhilo(savenamelo,savenamehi,ptlo,pthi,initial_condition):
    Cvals,WVvals,Wvals,zord = params_lowcheatgrass()
    param_grid = simulate(Cvals,WVvals,Wvals,initial_condition)
    make_plot_no_W(Cvals, WVvals, param_grid, zord, savenamelo, initial_condition,ptlo)
    Cvals,WVvals,Wvals,zord = params_highcheatgrass()
    param_grid = simulate(Cvals,WVvals,Wvals,initial_condition)
    make_plot_no_W(Cvals, WVvals, param_grid, zord, savenamehi, initial_condition,pthi)


def run01(savenamelo = "grid_results_locheatgrass_IC",savenamehi = "grid_results_hicheatgrass_IC",ptlo = (35,100,1.1),pthi = (150,100,0.6)):
    initial_condition = 0.1
    runhilo(savenamelo, savenamehi, ptlo, pthi, initial_condition)


def run10(savenamelo = "grid_results_locheatgrass_IC",savenamehi = "grid_results_hicheatgrass_IC",ptlo = (35,100,1.1),pthi = (150,100,0.6)):
    initial_condition = 1.0
    runhilo(savenamelo,savenamehi,ptlo,pthi,initial_condition)


if __name__ == "__main__":
    # run01()
    # run10()
    deltas = list(np.arange(0,0.701,0.05))
    results = simulate_for_fixed_pops(deltas)
    plot_deltas(results,deltas)


















