import numpy as np


def times(climate):
    x0 = 3
    x4 = 3
    x5 = 1
    if climate == 'am':
        x1 = 2.5
        x3 = 6
    elif climate in ('ro', 'ot'):
        x1 = 3.5
        x3 = 7
    else:
        raise ValueError("Climate not recognized.")
    return x0, x1, x3, x4, x5


def gamma(C, climate):
    # cheatgrass population (C) per m^2 to scaled wheat yield (climate dependent function)
    # parameters calculated from data; see fits_and_figs_from_data.py

    slope = 1.6726232412592983

    if climate == 'am':
        (n, A) = (-0.00323958, 1.35961716)
    elif climate == 'ot':
        (n, A) = (-0.00238718, 1.38985261)
    elif climate == 'ro':
        (n, A) = (-0.0018778, 1.05088302)
    else:
        raise ValueError("Climate not recognized.")

    return A * np.exp(n * slope * C)


def beta(source_spp, target_spp, source_pop, target_pop,alpha):
    if source_spp not in ('cg', 'wh') or target_spp not in ('cg', 'wh'):
        raise ValueError("Species not recognized.")
    if (source_spp, target_spp) == ('cg', 'cg'):
        A = 0.1
    else:
        A = 1.0
    # number plants
    S = source_pop
    T = target_pop
    if S > 0 and T > 0:
        return A / 2 * np.exp(-alpha / S - alpha / T)
    else:
        return 0


def beta_matrix(pops,alpha):
    # matrix order = [cheatgrass, volunteer wheat, wheat, new volunteer wheat]
    C, WV, W, NWV = pops
    bm = np.array([
        [beta("cg","cg",C,C,alpha), beta("wh","cg",WV,C,alpha), beta("wh","cg",W,C,alpha), 0.0],
        [beta("cg","wh",C,WV,alpha), beta("wh","wh",WV,WV,alpha), beta("wh","wh",W,WV,alpha),0.0],
        [beta("cg","wh",C,W,alpha), beta("wh","wh",WV,W,alpha), beta("wh","wh",W,W,alpha),0.0],
        [0.0, beta("wh","wh",WV,NWV,alpha),beta("wh","wh",W,NWV,alpha),0.0]
    ])
    return bm*pops


def plot_transmission():
    import matplotlib.pyplot as plt
    from matplotlib import rc
    rc("text",usetex=True)
    rc("axes",labelsize=16)
    rc("xtick",labelsize=14)
    rc("ytick",labelsize=14)
    pops = range(10, 500, 5)
    b = [beta('wh', 'wh', n, n) for n in pops]
    plt.plot(pops, b, color="k",linewidth=2)

    b = [beta('cg', 'cg', n, n) for n in pops]
    plt.plot(pops, b,color="gray",linewidth=2)

    plt.plot(pops,[0.05]*len(pops),color="k", linestyle="dashed",linewidth=1.0,dashes=(5, 10))
    plt.plot(pops,[0.5]*len(pops),color="k", linestyle="dashed",linewidth=1.0,dashes=(5, 10))
    plt.ylabel("Transmission rate")
    plt.xlabel(r"Number plants per m$^2$")
    plt.ylim([-0.02,0.52])

    plt.show()

if __name__ == "__main__":
    plot_transmission()