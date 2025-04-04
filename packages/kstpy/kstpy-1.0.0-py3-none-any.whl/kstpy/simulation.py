# -*- coding: utf-8 -*-

import random
from kstpy.helpers import domain
from kstpy.helpers import kstFrozenset
from kstpy.helpers import ParameterMisfitError


def simpleSimulation(structure, number, beta, gamma):
    """Simulate data from a structure according to the BLIM

    Parameters
    ----------

    structure: set 
        data basis for the simulation
    number: int
        number of response patterns to be simulated
    beta: float
        likelihood for careless errors
    gamma: float
        likelihood for lucky guesses

    Examples
    --------
    >>> from kstpy.data import xpl_basis
    >>> from kstpy.basics import constr
    >>> xpl_space = constr(xpl_basis)
    >>> simpleSimulation(xpl_space, 1000, 0.2, 0.1)
    """
    if not isinstance(structure, (set)):
        raise TypeError("structure must be a set of kstFrozensets.")
    if not isinstance(list(structure)[0], (kstFrozenset)):
        raise TypeError("The elements of structure must be of type kstFrozensets.")
    if not isinstance(number, int):
        raise TypeError("number must be an integer value.")
    if number <= 0:
        raise ValueError("number must be larger than zero.")
    if not (isinstance(beta, float) and isinstance(gamma, float)):
        raise TypeError("beta and gamma must be floats.")
    if beta < 0.0 or beta > 1.0:
        raise ValueError("beta must be within the [0,1] interval.")
    if gamma < 0.0 or gamma > 1.0:
        raise ValueError("gamma must be within the [0,1] interval.")
    d = domain(structure)
    sl = list(structure)
    simdata = list()
    for i in range(number):
        h = list()
        s = sl[random.randint(0,len(sl)-1)]
        for q in d:
            if (q in s):
                if random.random() > beta:
                    h.append(q)
            else:
                if random.random() < gamma:
                    h.append(q)
        sl.append(kstFrozenset(set(h)))
    return sl

def simulation(structure, number, beta, gamma):
    """Simulate data from a structure according to the BLIM

    Parameters
    ----------

    structure: set or list
        data basis for the simulation
    number: int
        number of response patterns to be simulated
    beta: dictionary (floats)
        likelihoods for careless errors
    gamma: dictionary (floats)
        likelihoods for lucky guesses

    Examples
    --------
    >>> from kstpy.data import xpl_basis
    >>> from kstpy.basics import constr
    >>> xpl_space = constr(xpl_basis)
    >>> beta = {"a":0.1, "b":0.2, "c":0.05, "d":0.15}
    >>> gamma = {"a":0.0, "b":0.25, "c":0.15, "d":0.1}
    >>> simulation(xpl_space, 1000, beta, gamma)
    """
    if not isinstance(structure, (list, set)):
        raise TypeError("structure must be a list or set of 'kstpy.helpers.kstFrozenset's.")
    if not isinstance(list(structure)[0], (kstFrozenset)):
        raise TypeError("The elements of structure must be of type 'kstpy.helpers.kstFrozenset'.")
    if not isinstance(number, int):
        raise TypeError("number must be an integer value.")
    if number <= 0:
        raise ValueError("number must be larger than zero.")
    if not isinstance(beta, dict):
        raise TypeError("beta must be a dictionary of item-probability pairs.")
    if not isinstance(gamma, dict):
        raise TypeError("gamma must be a dictionary of item-probability pairs.")
    for x in beta.values():
        if not isinstance(x, float):
            raise TypeError("The beta values must be floats.")
    for x in gamma.values():
        if not isinstance(x, float):
            raise TypeError("The gamma values must be floats.")
    if max(beta.values()) > 1 or min(beta.values()) < 0:
        raise ValueError("The beta values must be within the [0,1] interval.")
    if max(gamma.values()) > 1 or min(gamma.values()) < 0:
        raise ValueError("The gamma values must be within the [0,1] interval.")
    d = domain(structure)
    if sorted(list(beta.keys())) != d:
        raise ParameterMisfitError("beta does not fit to the domain of the structure.")
    if sorted(list(gamma.keys())) != d:
        raise ParameterMisfitError("gamma does not fit to the domain of the structure.")
    sl = list(structure)
    simdata = list()
    for i in range(number):
        h = list()
        s = sl[random.randint(0,len(sl)-1)]
        for q in d:
            if (q in s):
                if random.random() > beta[q]:
                    h.append(q)
            else:
                if random.random() < gamma[q]:
                    h.append(q)
        simdata.append(kstFrozenset(set(h)))
    return simdata
