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


def delta():
    delta1 = 0.7
    delta3 = 0.85
    return delta1, delta3


# def gamma1():
#     gamma11 = 0.0
#     gamma13 = 0.25
#     return gamma11, gamma13


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


def beta(source_spp, target_spp, source_pop, target_pop):
    if source_spp not in ('cg', 'wh') or target_spp not in ('cg', 'wh'):
        raise ValueError("Species not recognized.")
    if (source_spp, target_spp) == ('cg', 'cg'):
        A = 0.1
    else:
        A = 1.0
    # number plants per 1/10 m^2
    S = source_pop / 10
    T = target_pop / 10
    if S > 0 and T > 0:
        return A / 2 * np.exp(-1 / S - 1 / T)
    else:
        return 0


# def beta(source_spp, target_spp, source_pop, target_pop):
#     if source_spp not in ('cg', 'wh') or target_spp not in ('cg', 'wh'):
#         raise ValueError("Species not recognized.")
#     if (source_spp, target_spp) == ('cg', 'cg'):
#         A = 0.1
#     else:
#         A = 1.0
#     # number plants per 1/10 m^2
#     S = source_pop / 10
#     T = target_pop / 10
#     if S > 0 and T > 0:
#         return A * np.exp(-1 / S - 1 / T)
#     else:
#         return 0


def beta_matrix(pops):
    # matrix order = [cheatgrass, volunteer wheat, wheat, new volunteer wheat]
    C, WV, W, NWV = pops
    bm = np.array([
        [beta("cg","cg",C,C), beta("wh","cg",WV,C), beta("wh","cg",W,C), 0.0],
        [beta("cg","wh",C,WV), beta("wh","wh",WV,WV), beta("wh","wh",W,WV),0.0],
        [beta("cg","wh",C,W), beta("wh","wh",WV,W), beta("wh","wh",W,W),0.0],
        [0.0, beta("wh","wh",WV,NWV),beta("wh","wh",W,NWV),0.0]
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