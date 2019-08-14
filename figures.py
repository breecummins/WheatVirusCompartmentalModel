import SImodel as sim
import parameters
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

def simulate(Cvals,WVvals,Wvals,initial_condition,del1=0.7,alpha=10):
    numsteps = 1000
    param_grid = np.zeros((3, len(Cvals), len(WVvals), len(Wvals)))

    for h, climate in enumerate(["am", "ot", "ro"]):
        for i, C in enumerate(Cvals):
            for j, WV in enumerate(WVvals):
                for k, W in enumerate(Wvals):
                    param_grid[h, i, j, k] = sim.oneyear([C, WV, W, WV], climate,initial_condition, numsteps,(del1,del1+0.15),alpha)[0]
    return param_grid


def simulate_with_deltas(Cval,WVvals,Wval,initial_condition,deltas,alpha):
    numsteps = 1000
    param_grid = np.zeros((3, len(deltas), len(WVvals)))

    for h, climate in enumerate(["am", "ot", "ro"]):
        for j, WV in enumerate(WVvals):
            for l, del1 in enumerate(deltas):
                param_grid[h, l, j] = sim.oneyear([Cval, WV, Wval, WV], climate, initial_condition, numsteps,del1,alpha)[0]
    return param_grid


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

def params_deltas_volwheat_1():
    Cvals = 10
    WVvals = list(range(5, 101, 5))
    Wvals = 250
    alpha = 10
    del1 = np.arange(0,0.851,0.05)
    deltas = list(zip(del1,del1+0.15)) + [(1.0,1.0)]
    zord = {"ambient" : 3, "hot" : 5, "hot/dry" : 4}
    return Cvals,WVvals,Wvals,deltas,zord,alpha

def params_deltas_volwheat_2():
    Cvals = 10
    WVvals = list(range(5, 101, 5))
    Wvals = 250
    alpha = 1
    del1 = np.arange(0,0.851,0.05)
    deltas = list(zip(del1,del1+0.15)) + [(1.0,1.0)]
    zord = {"ambient" : 3, "hot" : 5, "hot/dry" : 4}
    return Cvals,WVvals,Wvals,deltas,zord,alpha


def params_deltas_volwheat_3():
    Cvals = 100
    WVvals = list(range(5, 101, 5))
    Wvals = 250
    alpha = 10
    del1 = np.arange(0,0.851,0.05)
    deltas = list(zip(del1,del1+0.15)) + [(1.0,1.0)]
    zord = {"ambient": 3, "hot": 5, "hot/dry": 4}
    return Cvals, WVvals, Wvals, deltas, zord, alpha


def params_deltas_volwheat_4():
    Cvals = 100
    WVvals = list(range(5, 101, 5))
    Wvals = 250
    alpha = 1
    del1 = np.arange(0,0.851,0.05)
    deltas = list(zip(del1,del1+0.15)) + [(1.0,1.0)]
    zord = {"ambient": 3, "hot": 5, "hot/dry": 4}
    return Cvals, WVvals, Wvals, deltas, zord, alpha


def make_plot_no_W(Cvals,WVvals,param_grid,zord,savename,init_cond,pt):
    X, Y = np.meshgrid(Cvals,WVvals)

    fig = plt.figure()
    ax = fig.gca(projection='3d')
    zlim=[0.0,1.35]

    Z3 = np.squeeze(param_grid[2:,:,:,:1])
    ax.plot_surface(X.transpose(), Y.transpose(), Z3,label="ROS+OTC",color="firebrick",zorder=zord["hot/dry"])
    p3 = plt.Rectangle((0, 0), 1, 1, fc="firebrick")


    Z1 = np.squeeze(param_grid[:1,:,:,:1])
    ax.plot_surface(X.transpose(), Y.transpose(), Z1,label="AMB",color="darksalmon",zorder=zord["ambient"])
    p1 = plt.Rectangle((0, 0), 1, 1, fc="darksalmon")

    Z2 = np.squeeze(param_grid[1:2,:,:,:1])
    ax.plot_surface(X.transpose(), Y.transpose(), Z2,label="OTC",color="red",zorder=zord["hot"])
    p2 = plt.Rectangle((0, 0), 1, 1, fc="red")

    f = lambda x,y,z: proj3d.proj_transform(x,y,z, ax.get_proj())[:2]
    ax.legend([p1,p2,p3],['AMB','OTC','ROS+OTC'],loc="lower left", bbox_to_anchor=f(*pt),
              bbox_transform=ax.transData)
    ax.set_xlabel(r"B. tectorum")
    ax.set_ylabel(r"volunteer wheat")
    ax.set_zlabel("winter wheat yield")
    ax.set_zlim(zlim)
    plt.savefig(savename+"_{:0.2f}".format(init_cond).replace(".","_")+".pdf")
    # plt.show()


def make_plot_no_W_no_C(deltas,WVvals,param_grid,zord,savename,init_cond,pt):
    del1,del2 = zip(*deltas)
    X, Y = np.meshgrid([1-d for d in del1[:-1]],WVvals)

    fig = plt.figure()
    ax = fig.gca(projection='3d')
    zlim=[0.0,1.35]

    Z3 = np.squeeze(param_grid[2:,:-1,:])
    ax.plot_surface(X.transpose(), Y.transpose(), Z3,label="ROS+OTC",color="firebrick",zorder=zord["hot/dry"])
    p3 = plt.Rectangle((0, 0), 1, 1, fc="firebrick")


    Z1 = np.squeeze(param_grid[:1,:-1,:])
    ax.plot_surface(X.transpose(), Y.transpose(), Z1,label="AMB",color="darksalmon",zorder=zord["ambient"])
    p1 = plt.Rectangle((0, 0), 1, 1, fc="darksalmon")

    Z2 = np.squeeze(param_grid[1:2,:-1,:])
    ax.plot_surface(X.transpose(), Y.transpose(), Z2,label="OTC",color="red",zorder=zord["hot"])
    p2 = plt.Rectangle((0, 0), 1, 1, fc="red")

    f = lambda x,y,z: proj3d.proj_transform(x,y,z, ax.get_proj())[:2]
    ax.legend([p1,p2,p3],['AMB','OTC','ROS+OTC'],loc="lower left", bbox_to_anchor=f(*pt),
              bbox_transform=ax.transData)
    ax.set_xlabel(r"$\delta$")
    ax.set_ylabel(r"volunteer wheat")
    ax.set_zlabel("winter wheat yield")
    ax.set_zlim(zlim)
    plt.savefig(savename+"_{:0.2f}".format(init_cond).replace(".","_")+".pdf")
    # plt.show()


def plot_delta_climate(deltas,delta_inds,WVvals,Cvals,param_grid,savename,initial_condition):
    plt.figure()

    ref = np.squeeze(param_grid[:1,-1:,:])

    for i in delta_inds:
        Z3 = np.squeeze(param_grid[:1,i:i+1,:])
        Z4 = np.squeeze(Z3-ref)
        plt.plot(WVvals,Z4,linewidth=2,label=r"$\delta$ = {:.02f}".format(1-deltas[i]))

    # am = np.squeeze(clim_grid[:1,:1,:])
    # ro = np.squeeze(clim_grid[2:,:1,:])
    clim_diff = parameters.gamma(Cvals, "amb") - parameters.gamma(Cvals, "ro")
    plt.plot(WVvals,[clim_diff]*len(WVvals),"k",linewidth=2,label="AMB - ROS+OTC")

    lgd = plt.legend(fontsize=16,bbox_to_anchor=(1,1))
    plt.ylim([-0.5,0])
    plt.xlabel(r"volunteer wheat plants per m$^2$")
    plt.ylabel(r"$\Delta$ ambient winter wheat yield")
    plt.savefig(savename+"_{:0.2f}".format(initial_condition).replace(".","_")+".pdf",bbox_inches="tight",bbox_extra_artists=(lgd,))
    # plt.show()


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


def rundeltas(param_func,delta_inds,pt):
    initial_condition = 0.5
    Cvals, WVvals, Wvals, deltas, zord,alpha = param_func()
    param_grid = simulate_with_deltas(Cvals,WVvals,Wvals,initial_condition,deltas,alpha)
    make_plot_no_W_no_C(deltas, WVvals, param_grid, zord, "grid_results_deltas_C{}_alpha{}_IC".format(Cvals,alpha), initial_condition, pt)
    # clim_grid = simulate_with_deltas(Cvals,WVvals,Wvals,0.0,[1.0],alpha)
    plot_delta_climate(deltas,delta_inds,WVvals, Cvals, param_grid,"delta_vs_climate_C{}_alpha{}_IC".format(Cvals,alpha),initial_condition)
    return param_grid


def multiple_delta_runs():
    pg=rundeltas(params_deltas_volwheat_1,[-19,-17,-15,-13,-11,-9,-7,-6,-5,-3],pt=(0.5,100,0.8))
    # pg=rundeltas(params_deltas_volwheat_2,[-9,-7,-6,-5,-2],pt=(0.5,100,0.8))
    pg=rundeltas(params_deltas_volwheat_3,[-19,-17,-15,-13,-11,-9,-7,-6,-5,-3],pt=(0.5,100,0.5))
    # pg=rundeltas(params_deltas_volwheat_4,[-9,-7,-6,-5,-2],pt=(0.5,100,0.5))

if __name__ == "__main__":
    multiple_delta_runs()
    # run01()
    # run10()


















