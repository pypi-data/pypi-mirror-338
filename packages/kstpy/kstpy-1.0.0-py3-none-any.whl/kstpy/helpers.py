# -*- coding: utf-8 -*-
"""
Created on Sun Mar  9 13:03:53 2025

@author: hockemey
"""
import more_itertools as mi

class kstFrozenset(frozenset):
    """
    kstFrozenset is a derivative of the frozenset class.
    
    The main reason for its existance is the print function which
    does not show the class anymore. Set operands (\|, &, ^, and -)
    have also been re-defined to produce kstFrozensets.
    """
    def __repr__(self):
        if self == frozenset({}):
            return "\u2205"
        else:
            return set(self).__repr__()

    def __str__(self):
        if self == frozenset({}):
            return "{}"
        else:
            return set(self).__str__()
    
    def __or__(self, value):
        return kstFrozenset(frozenset(self) | frozenset(value))
    
    def __and__(self, value):
        return kstFrozenset(frozenset(self) & frozenset(value))
    
    def __sub__(self, value):
        return kstFrozenset(frozenset(self) - frozenset(value))
    
    def __xor__(self, value):
        return kstFrozenset(frozenset(self) ^ frozenset(value))
    

class ParameterMisfitError(RuntimeError):
    """ ParameterMisfitError is a sub class of RuntimeError.
    
    It should be raised when parameters in a function call do not fit together,
    e.g. in size.
    """
    def __init__(self, msg="Parameters do not fit"):
        self.msg = msg
        super().__init__(self.msg)

    def __str__(self):
        return f'{self.msg}'


def itemname(num):
    """Return an Itemname based on the item number

    For smaller numbers it is a letter a..z. For larger numbers, up to three
    lettersa may be used, i.e. in the end we have a..z, aa..zz, aaa.zzz.
    This gives so far up to 18278 items that can be named with this function.

    Parameters
    ----------
    num: int

    Returns
    -------
    Generated item name (str)
    """
    if not isinstance(num, int):
        raise TypeError("num must be an integer number.")
    if (num < 0):
        raise ValueError("Sorry, no numbers below zero")
    elif (num < 26):
         return(chr(num+97))
    elif (num < 702):
         return(chr((num//26)+97)+chr((num%26)+97)) 
    elif (num < 18278):
         return(chr((num//676)+97)+chr((num//26)+97)+chr((num%26)+97)) 
    else:
         raise ValueError("So far limited to 17576 items")# -*- coding: utf-8 -*-


def nitemnames(count):
    """ Return a list of `count` itemnames
    
    Parameters
    ----------

    count: int

    Returns
    ------
    list of itemnames
    """
    if not isinstance(count, int):
        raise TypeError("count must be an integer number.")
    if (count < 0):
        raise ValueError("Sorry, no numbers below zero")
    return list([itemname(i) for i in range(count)])

def domain(structure):
    """ Determine the domain of a set/list of kstFrozensets

    Parameters
    ----------
    structure: set of kstFrozensets

    Returns
    -------
    Domain of structure as vector of items
    """
    if not isinstance(structure, set):
        raise TypeError("structure must bed a set (of kstFrozenset's).")
    for x in structure:
        if not isinstance(x, kstFrozenset):
            raise TypeError("The elements of structure must be kstFrozenset's.")
    dom = set({})
    for s in structure:
        dom = dom | s
    return sorted(list(dom))

def srdomain(sr):
    """ Determine the domain of a surmise relation

    Parameters
    ----------

    sr: set of tuples defining the surmise relation

    Returns
    ------
    domain underlying the surmise relation as sorted list
    """
    if not isinstance(sr, set):
        raise TypeError("sr must be a set.")
    for x in sr:
        if not isinstance(x, tuple) or not len(x) == 2:
            raise TypeError("The elements of sr must be 2-tuples.")
    dom = set({})
    for p in sr:
        dom = dom | set(p)
    return sorted(list(dom))

def reduceSR(sr):
    """
    Remove transitivities from a (surmise) relation
    
    Parameters
    ----------
    
    sr: set (of 2-tuples)

    Returns
    -------

    Reduced relation
    """
    if not isinstance(sr, set):
        raise TypeError("sr must be a set.")
    for x in sr:
        if not isinstance(x, tuple) or not len(x) == 2:
            raise TypeError("The elements of sr must be 2-tuples.")
    src = sr.copy()
    d = srdomain(src)
    for i in d:
        for j in d:
            if (i != j) & ((i,j) in sr):
                for k in d:
                    if (i != k) & (j != k) & ((i,k) in sr) & ((j,k) in sr):
                        src.discard((i,k))
    return(src)


def powerset(domain):
    """ Determine the powerset for a domain
    
    Parameters
    ----------
    domain: list

    Returns
    ------

    Set of kstFrozensets
        Power set

    Examples
    --------
    >>> d = list(["a", "b", "c", "d"])
    >>> powerset(d)
    """
    if not isinstance(domain, list):
        raise TypeError("domain must be a list.")
    l = list(mi.powerset_of_sets(domain))
    res = set({})
    for i in l:
        res.add(kstFrozenset(i))
    return res

def vector2kstFrozenset(v, d):
    """ Determine a kstFrozenset corresponding to a binary vector
    
    Parameters
    ----------

    v: list of '0's and '1's
        Vector representation of the set to be converted
    d: List of items
        Domain

    Returns
    ------

    kstFrozenset
        Set representation

    Examples
    --------
    >>> v = list([1,0,0,1])
    >>> d = list(["a", "b", "c", "d"])
    >>> vector2kstFrozenset(v,d)
    """
    if not isinstance(v, list):
        raise TypeError("v must be a list.")
    for x in v:
        if x != 0 and x != 1:
            raise ValueError("v must be a list of zeros and ones.")
    if not isinstance(d, list):
        raise TypeError("d must be a list (of items).")
    if (len(v) != len(d)):
        raise ParameterMisfitError("Vector v and domain d do not match!")
    s = set({})
    for i in range(len(v)):
        if (v[i]!= 0):
            s.add(d[i])
    return kstFrozenset(s)

def kstFrozenset2vector(s, d):
    """ Determine a binary vector describing a kstFrozenset
    
    Parameters
    ----------

    s: kstFrozenset
        Set to be converted
    d: List of items
        Domain

    Returns
    ------

    List
        Binary vector (list of '0's and '1's) of length |d|

    Examples
    --------
    >>> from kstpy.helpers import kstFrozenset
    >>> s = kstFrozenset({"a", "b"})
    >>> d = list(["a", "b", "c", "d"])
    >>> kstFrozenset2vector(s, d)
    """
    if not isinstance(s, kstFrozenset):
        raise TypeError("s must be a kstFrozenset.")
    if not isinstance(d, list):
        raise TypeError("d must be a (sorted) list of items.")
    if (not(s <= set(d))):
        raise ParameterMisfitError("Set s and domain d do not match!")
    v = ""
    for i in d:
        if i in s:
            v = v + "1"
        else:
            v = v + "0"
    return v
