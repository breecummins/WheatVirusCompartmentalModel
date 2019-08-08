import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import least_squares

from matplotlib import rc
rc('text',usetex=True)
fontsize=16
rc('axes', labelsize=fontsize)    # fontsize of the x and y labels
rc('xtick', labelsize=14)    # fontsize of the tick labels
rc('ytick', labelsize=14)    # fontsize of the tick labels
rc('legend', fontsize=fontsize)    # legend fontsize


################################
# generic plotting function
################################

def plot_data(xpts,ypts,more_than_one_pts=False,legend = False,more_than_one_curve=False,x=None,curve=None, xlabel="", ylabel="", title="",ylim=None,xlim=None,savefile="",color="blue",show=False,verticals=None):
    plt.figure()
    ax = plt.gca()
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
        if not legend:
            plt.plot(xpts, ypts, linestyle="", marker="o", color=color)
        else:
            plt.plot(xpts, ypts, linestyle="", marker="o", color=color,label=legend[0])
            plt.legend()
    if more_than_one_curve:
        if isinstance(color,str):
            color = [color]*len(xpts)
        for (xp, yp, c) in zip(x, curve, color):
            plt.plot(xp, yp, color=c)
    elif x is not None and curve is not None:
        if not isinstance(color,str):
            plt.plot(x,curve)
        else:
            plt.plot(x,curve,color=color)
    if verticals is not None:
        if ylim is None:
            ylim = ax.get_ylim()
        for v in verticals:
            plt.plot([v]*2,ylim,linestyle="-",color="k")
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    if xlim:
        plt.xlim(xlim)
    if ylim:
        plt.ylim(ylim)
    if savefile:
        plt.savefig(savefile,bbox_inches="tight")
    if show:
        plt.show()
    else:
        plt.close()


def plot_curves_only(x,curve,legend = False,more_than_one_curve=False,xlabel="",ylabel="",title="",ylim=None,xlim=None,savefile="",color="blue",show=False,verticals=None):
    plt.figure()
    if more_than_one_curve:
        if isinstance(color,str):
            color = [color]*len(xpts)
        if not legend:
            for (xp, yp, c) in zip(x, curve, color):
                plt.plot(xp, yp, color=c)
        else:
            for (xp, yp, c,lab) in zip(x, curve, color,legend):
                plt.plot(xp, yp, color=c,label=lab)
            plt.legend()
    else:
        if not isinstance(color,str) and not legend:
            plt.plot(x,curve)
        elif not legend:
            plt.plot(x,curve,color=color)
        elif not isinstance(color,str):
            plt.plot(x, curve,label=legend[0])
        else:
            plt.plot(x, curve, color=color,label=legend[0])
    if verticals is not None:
        if ylim is None:
            ylim = ax.get_ylim()
        for v in verticals:
            plt.plot([v]*2,ylim,linestyle="-",color="k")
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    if xlim:
        plt.xlim(xlim)
    if ylim:
        plt.ylim(ylim)
    if savefile:
        plt.savefig(savefile,bbox_inches="tight")
    if show:
        plt.show()
    else:
        plt.close()


def plot_data_with_textbox(xpts,ypts,params,curve_type,more_than_one_pts=False,legend = False,more_than_one_curve=False,x=None,curve=None,xlabel="",ylabel="",title="",ylim=None,xlim=None,savefile="",color="blue",show=False):
    fig,ax = plt.subplots()
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
        if not isinstance(color,str):
            plt.plot(x,curve)
        else:
            plt.plot(x,curve,color=color)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    if xlim:
        plt.xlim(xlim)
    if ylim:
        plt.ylim(ylim)

    # make text box
    props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)

    if curve_type == "exp":
        amp = "{:.02f}".format(params[0])
        exp = "{:.04f}".format(params[1])
        textstr = r'$y = '+amp+'e^{'+exp+'x}$'
        ax.text(0.65, 0.95, textstr, transform=ax.transAxes, fontsize=16,
                verticalalignment='top', bbox=props)
    elif curve_type == "lin":
        textstr = r'$y = {:.02f}x$'.format(params[0])
        ax.text(0.7, 0.95, textstr, transform=ax.transAxes, fontsize=16,
                verticalalignment='top', bbox=props)
    elif curve_type == "exp_lin":
        amp = "{:.02f}".format(params[0])
        exp = "{:.04f}".format(params[1])
        slope = "{:.02f}".format(params[2])
        textstr = r'$y = ' + amp + 'e^{' + exp + '('+slope+')x}$'
        ax.text(0.575, 0.95, textstr, transform=ax.transAxes, fontsize=16,
            verticalalignment='top', bbox=props)


    # place a text box in upper right in axes coords


    if savefile:
        plt.savefig(savefile,bbox_inches="tight")
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

