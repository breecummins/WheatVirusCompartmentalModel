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


def gamma1():
    gamma11 = 0.7
    gamma13 = 0.85
    return gamma11, gamma13


def gamma2(C, climate):
    # cheatgrass population (C) to wheat yield (climate dependent function)

    def cg_plants_to_cg_biomass(x):
        (A, K, n) = (1.53784145e+03, 1.39634038e+06, 2.37217919e+00)
        return A * x ** n / (K + x ** n)

    if climate == 'am':
        (n, A) = (-0.00431991, 0.71898844)
    elif climate == 'ot':
        (n, A) = (-0.00303991, 0.73144328)
    elif climate == 'ro':
        (n, A) = (-0.00237851, 0.55373904)
    else:
        raise ValueError("Climate not recognized.")

    return A * np.exp(n * cg_plants_to_cg_biomass(C))


def beta(source_spp, target_spp, source_pop, target_pop, field_size):
    if source_spp not in ('cg', 'wh') or target_spp not in ('cg', 'wh'):
        raise ValueError("Species not recognized.")
    if (source_spp, target_spp) == ('cg', 'cg'):
        A = 0.1
    else:
        A = 1.0
    # number plants per 1/10 m^2
    S = source_pop / field_size / 10
    T = target_pop / field_size / 10
    return A / 2 * np.exp(-1 / S - 1 / T)


def plot_transmission():
    import matplotlib.pyplot as plt
    pops = range(100, 2500000, 100)
    b = [beta('wh', 'wh', n, n, 10000) for n in pops]
    plt.plot(pops, b)

    b = [beta('cg', 'cg', n, n, 10000) for n in pops]
    plt.plot(pops, b)
    plt.show()

if __name__ == "__main__":
    plot_transmission()