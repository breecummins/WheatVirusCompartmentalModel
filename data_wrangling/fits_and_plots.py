import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import least_squares

################################
# generic plotting function
################################

def plot_data(xpts,ypts,more_than_one_pts=False,legend = False,more_than_one_curve=False,x=None,curve=None,xlabel="",ylabel="",title="",ylim=None,xlim=None,savefile="",color="blue",show=False):
    plt.figure()
    if more_than_one_pts:
        if isinstance(color,str):
            color = [color]*len(xpts)
        if not legend:
            for (xp, yp, c) in zip(xpts, ypts, color):
                plt.plot(xp, yp, linestyle="", marker="o", color=c)
        else:
            for (xp,yp,c,lab) in zip(xpts,ypts,color,legend):
                plt.plot(xp,yp,linestyle="",marker="o",color=c,label=lab)
            plt.legend()
    else:
        plt.plot(xpts, ypts, linestyle="", marker="o", color=color)
    if more_than_one_curve:
        if isinstance(color,str):
            color = [color]*len(xpts)
        for (xp, yp, c) in zip(x, curve, color):
            plt.plot(xp, yp, color=c)
    elif x is not None and curve is not None:
        plt.plot(x,curve)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    if xlim:
        plt.xlim(xlim)
    if ylim:
        plt.ylim(ylim)
    if savefile:
        plt.savefig(savefile)
    if show:
        plt.show()
    else:
        plt.close()


################################
# data fitting
################################

def lin_curve(p,x):
    # good IC = np.array([1])
    return p[0]*x

def exp_curve(p,x):
    # good IC = np.array([1,-1])
    return p[0]*np.exp(p[1]*x)

def log_curve(p,x):
    # good IC = np.array([1,-1])
    return p[0] * (1 + np.exp(-x))**(p[1])

def hill_curve(p,x):
    # good IC = np.array([1,2,1])
    return p[0] * x**p[1] / (p[2]**p[1] + x**p[1])

def fit(xpts,ypts,curve,IC):
    def func(p,x,y):
        return curve(p,x) -y
    p = least_squares(func,IC,args=(xpts, ypts))
    return p["x"]

def get_curve(xpts,ypts,curve,IC,x):
    p = fit(xpts,ypts,curve,IC)
    return curve(p,x)

