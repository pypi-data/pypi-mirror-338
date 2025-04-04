# -*- coding: utf-8 -*-

from kstpy.helpers import kstFrozenset
from kstpy.helpers import ParameterMisfitError
from kstpy.helpers import domain
from kstpy.helpers import srdomain
from kstpy.helpers import powerset
import collections as c

def distvec(data, structure):
    """Compute a vector of distances from response patterns to a knowledge structure

    Parameters
    ----------
    data: list
        List of kstFrozensets containing response patterns
    structure: set
        Family of kstFrozensets - the knowledge structure

    Returns
    -------
    List
        Vector of distances between response patterns and knowledge structure

    Examples
    --------
    >>> from kstpy.data import xpl_basis
    >>> from kstpy.basics import constr
    >>> from kstpy.simulation import simpleSimulation
    >>> xpl_space = constr(xpl_basis)
    >>> xpl_data = simpleSimulation(xpl_space, 1000, 0.15, 0.1)
    >>> distvec(xpl_data, xpl_space)
    """
    if not isinstance(data, list):
        raise TypeError("data must bed a set (of kstFrozenset's).")
    for x in data:
        if not isinstance(x, kstFrozenset):
            raise TypeError("The elements of data must be kstFrozenset's.")
    if not isinstance(structure, set):
        raise TypeError("structure must bed a set (of kstFrozenset's).")
    for x in structure:
        if not isinstance(x, kstFrozenset):
            raise TypeError("The elements of structure must be kstFrozenset's.")

    ddom = domain(data)
    sdom = domain(structure)
    if (ddom != sdom):
        raise ParameterMisfitError("Incompativble domains")

    dvec = []
    for pattern in data:
        di = len(ddom)
        for state in structure:
            d = len(pattern ^ state)
            di = min(di, d)
        dvec.append(di)
    return dvec


def difreq(data, structure):
    """Determine a vector of frequencies of distances between a set of response patterns and a knowledge structure

    Parameters
    ----------
    data: list
        List of kstFrozensets containing response patterns
    structure: set
        Family of kstFrozensets - the knowledge structure

    Returns
    -------
    List
        Vector of distance frequencies
    
    Examples
    --------
    >>> from kstpy.data import xpl_basis
    >>> from kstpy.basics import constr
    >>> from kstpy.simulation import simpleSimulation
    >>> xpl_space = constr(xpl_basis)
    >>> xpl_data = simpleSimulation(xpl_space, 1000, 0.15, 0.1)
    >>> difreq(xpl_data, xpl_space)
"""
    if not isinstance(data, list):
        raise TypeError("data must bed a set (of kstFrozenset's).")
    for x in data:
        if not isinstance(x, kstFrozenset):
            raise TypeError("The elements of data must be kstFrozenset's.")
    if not isinstance(structure, set):
        raise TypeError("structure must bed a set (of kstFrozenset's).")
    for x in structure:
        if not isinstance(x, kstFrozenset):
            raise TypeError("The elements of structure must be kstFrozenset's.")

    dvec = distvec(data, structure)
    cnt = c.Counter(dvec)
    di = [cnt[x] for x in sorted(cnt.keys())]
    return di


def di(data, structure):
    """Determine the Discrepancy Index
    
     Parameters
    ----------
    data: list
        List of kstFrozensets containing response patterns
    structure: set
        Family of kstFrozensets - the knowledge structure

    Returns
    -------
    Float
        Discrepancy Index
    
    Examples
    --------
    >>> from kstpy.data import xpl_basis
    >>> from kstpy.basics import constr
    >>> from kstpy.simulation import simpleSimulation
    >>> xpl_space = constr(xpl_basis)
    >>> xpl_data = simpleSimulation(xpl_space, 1000, 0.15, 0.1)
    >>> di(xpl_data, xpl_space)
   """
    if not isinstance(data, list):
        raise TypeError("data must bed a set (of kstFrozenset's).")
    for x in data:
        if not isinstance(x, kstFrozenset):
            raise TypeError("The elements of data must be kstFrozenset's.")
    if not isinstance(structure, set):
        raise TypeError("structure must bed a set (of kstFrozenset's).")
    for x in structure:
        if not isinstance(x, kstFrozenset):
            raise TypeError("The elements of structure must be kstFrozenset's.")

    dvec = distvec(data, structure)
    index = float(sum(dvec)) / float(len(dvec))
    return index


def da(data, structure):
    """Determine the Distance Agreement coefficient
    
    Parameters
    ----------
    data: list
        List of kstFrozensets containing response patterns
    structure: set
        Family of kstFrozensets - the knowledge structure

    Returns
    -------
    Float
        Distance Agreement coefficient
    
    Examples
    --------
    >>> from kstpy.data import xpl_basis
    >>> from kstpy.basics import constr
    >>> from kstpy.simulation import simpleSimulation
    >>> xpl_space = constr(xpl_basis)
    >>> xpl_data = simpleSimulation(xpl_space, 1000, 0.15, 0.1)
    >>> da(xpl_data, xpl_space)
    """
    if not isinstance(data, list):
        raise TypeError("data must bed a set (of kstFrozenset's).")
    for x in data:
        if not isinstance(x, kstFrozenset):
            raise TypeError("The elements of data must be kstFrozenset's.")
    if not isinstance(structure, set):
        raise TypeError("structure must bed a set (of kstFrozenset's).")
    for x in structure:
        if not isinstance(x, kstFrozenset):
            raise TypeError("The elements of structure must be kstFrozenset's.")

    ddat = di(data, structure)
    p = powerset(domain(structure))
    dpot = di(p, structure)
    return float(ddat) / float(dpot)

def gamma(data, relation):
    """ Compute the _gamma coefficient_ for a surmise relation and a set of data

    The gamma index is defined as (NC - ND) / (NC + ND) where NC is the number 
    of concordant pairs and ND the number of discordant pairs.
    
    Parameters
    ----------

    data: list of kstFrozensets
        Response patterns
    relation: set of 2-tuples
        Surmise relation to be validated

    Returns
    -------
    Float
        Gamma index
    
    Examples
    --------
    >>> from kstpy.data import xpl_basis
    >>> from kstpy.basics import surmiserelation
    >>> from kstpy.simulation import simpleSimulation
    >>> xpl_sr = surmiserelation(xpl_basis)
    >>> xpl_data = simpleSimulation(xpl_space, 1000, 0.15, 0.1)
    >>> gamma(xpl_data, xpl_sr)
    """
    if not isinstance(data, list):
        raise TypeError("data must bed a set (of kstFrozenset's).")
    for x in data:
        if not isinstance(x, kstFrozenset):
            raise TypeError("The elements of data must be kstFrozenset's.")
    if not isinstance(relation, set):
        raise TypeError("relation mus be a set of 2-tuples.")
    for x in relation:
        if not isinstance(x, tuple) or len(x) != 2:
            raise TypeError("The elements of relation must be 2-tuples.")
    if domain(data) != srdomain(relation):
        raise ParameterMisfitError("differfent domains in data and structure!")

    nc = 0
    nd = 0
    for pair in relation:
        for pattern in data:
            if pair[0] in pattern and not pair[1] in pattern:
                nc += 1
            elif pair[1] in pattern and not pair[0] in pattern:
                nd += 1
    gamma = float(nc - nc) / float (nc + nd)
    return gamma


def vc(data, relation):
    """ Compute the _Violational Coefficient_ for a data set against a surmise relation
    
    Parameters
    ----------

    data: list of kstFrozensets
        Response patterns
    relation: set of 2-tuples
        Surmise relation to be validated

    Returns
    -------
    Float
        Violational Coefficient
    
    Examples
    --------
    >>> from kstpy.data import xpl_basis
    >>> from kstpy.basics import surmiserelation
    >>> from kstpy.simulation import simpleSimulation
    >>> xpl_sr = surmiserelation(xpl_basis)
    >>> xpl_data = simpleSimulation(xpl_space, 1000, 0.15, 0.1)
    >>> vc(xpl_data, xpl_sr)
    """
    if not isinstance(data, list):
        raise TypeError("data must bed a set (of kstFrozenset's).")
    for x in data:
        if not isinstance(x, kstFrozenset):
            raise TypeError("The elements of data must be kstFrozenset's.")
    if not isinstance(relation, set):
        raise TypeError("relation mus be a set of 2-tuples.")
    for x in relation:
        if not isinstance(x, tuple) or len(x) != 2:
            raise TypeError("The elements of relation must be 2-tuples.")
    if domain(data) != srdomain(relation):
        raise ParameterMisfitError("differfent domains in data and structure!")

    nd = 0
    for pair in relation:
        for pattern in data:
            if pair[1] in pattern and not pair[0] in pattern:
                nd += 1
    vc = float(nd) / float(len(data) * (len(relation) - len(srdomain(relation))))
    return vc
