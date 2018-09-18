import numpy as np
from parameters import *


def forwardEuler():
    pass


def oneyear(pops,climate,infected = np.array([0,0.10,0]),field_size=10000):
    # order is cheatgrass, volunteer wheat, wheat
    x0, x1, x3, x4, x5 = times(climate)
    # x0 time period can be calculated exactly
    cst = (1 - infected[1])/infected[1]
    b = beta('wh','wh',pops[1],pops[1],field_size)
    infected[1] = np.exp(b*x0) / ( np.exp(b*x0) + cst )
    # now for x1 time period
    # construct matrix



def multiyear():
    pass


def calculate_wheat_yield(C,V1,V3,climate):
    '''

    :param C: cheat grass population
    :param V1: proportion of infected wheat after time period x1
    :param V3: proportion of infected wheat after time period x3
    :param climate: 'am' (ambient), 'ot' (hot), or 'ro' (hot/dry)
    :return: wheat yield
    '''
    gamma11,gamma13 = production_rates()
    return gamma2(C,climate) * (gamma11 * V1 + gamma13 * (V3 - V1) + 1 - V3)