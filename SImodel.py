import numpy as np
import parameters as pm


def forwardEuler(A,infected,T,numsteps):
    '''
    Formula: infected(n+1) = infected(n) + delta_time(rate)*infected(n)

    :param A: Matrix of constant transmission rates times current populations
    :param infected: Proportion of infected individuals at the start of the time period
    :param T: Time period
    :param numsteps: Number of forward Euler steps to take in one time unit
    :return: A vector of the proportion infected at the end of the time period
    '''
    for _ in range(int(T*numsteps)):
        rate = A * (1 - infected[:].reshape(A.shape[0],1))
        infected = (np.eye(A.shape[0]) + (1./numsteps)* rate).dot(infected[:])
    return infected


def calculate_wheat_yield(C,V1,V3,climate,deltas):
    '''

    :param C: cheat grass population
    :param V1: proportion of infected wheat after time period x1
    :param V3: proportion of infected wheat after time period x3
    :param climate: 'am' (ambient), 'ot' (hot), or 'ro' (hot/dry)
    :return: wheat yield
    '''
    (delta1, delta3) = deltas
    return pm.gamma(C,climate) * (delta1 * V1 + delta3 * (V3 - V1) + 1 - V3)


def oneyear(pops,climate,vol_wheat_infected_IC,numsteps,deltas,alpha):
    '''

    :param pops: list or numpy array of four populations in the order of [cheatgrass, volunteer wheat, wheat, new volunteer wheat]
    :param climate: "am" for ambient, "ot" for hot, "ro" for hot and dry
    :param vol_wheat_infected_IC: initial condition -- the proportion of infected volunteer wheat at harvest
    :param numsteps: number of steps to take per time unit in the forward Euler solver
    :return: the projected wheat yield at the end of the year and the proportion of new infected volunteer wheat
    '''
    # if there is no infected volunteer wheat, calculate the yield just under climate
    if vol_wheat_infected_IC == 0:
        wh_yield = calculate_wheat_yield(pops[0], 0, 0, climate, deltas)
        return wh_yield, 0
    bm = pm.beta_matrix(pops,alpha)
    x0, x1, x3, x4, x5 = pm.times(climate)
    # x0 time period can be calculated exactly
    cst = (1 - vol_wheat_infected_IC)/vol_wheat_infected_IC
    b = pm.beta('wh','wh',pops[1],pops[1],alpha)
    V0 = np.array([0.0, np.exp(b*x0) / ( np.exp(b*x0) + cst ), 0.0])
    # now for x1 time period, populations cheatgrass, vol wheat, wheat (new vol wheat not up yet)
    A = bm[:-1,:-1] / sum(pops[:-1])
    # fall spread
    V1 = forwardEuler(A,V0,x1,numsteps)
    # spring spread
    V3 = forwardEuler(A,V1,x3,numsteps)
    # spread after plant growth has stopped
    V4 = forwardEuler(A, V3, x4,numsteps)
    # spread into new volunteer wheat, cheatgrass has died and is not active in spread, gives new IC for next year
    A = bm[1:,1:] / sum(pops[1:])
    new_IC = forwardEuler(A,V4,x5,numsteps)
    wh_yield = calculate_wheat_yield(pops[0], V1[2], V3[2], climate,deltas)
    return wh_yield, new_IC


def multiyear(populations,climates,deltas,alpha,IC,numsteps=10000):
    '''

    :param populations: A length N list of numpy arrays of length 4 containing the populations per m^2 for (in order) [cheatgrass, volunteer wheat, wheat, new volunteer wheat]
    :param climates: A length N list of climates, "am", "ot", and "ro", for ambient, hot, hot/dry respectively
    :param IC: initial condition -- the proportion of infected volunteer wheat at harvest
    :param numsteps: number of steps to take per time unit in the forward Euler solver
    :return: A length N vector of projected wheat yields for the given populations and climates
    '''
    years = list(zip(populations,climates))
    ystr = "Running for {} years.".format(len(years)) if len(years) > 1 else "Running for 1 year."
    print(ystr)
    yields = []
    for pops,climate in years:
        wh_yield, IC = oneyear(pops,climate,IC,numsteps,deltas,alpha)
        yields.append(wh_yield)
    return yields


