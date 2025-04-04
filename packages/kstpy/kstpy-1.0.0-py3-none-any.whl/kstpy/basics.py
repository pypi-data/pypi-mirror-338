# -*- coding: utf-8 -*-
from kstpy.helpers import kstFrozenset
from kstpy.helpers import ParameterMisfitError
from kstpy.helpers import domain
from kstpy.helpers import srdomain

def constr(structure):
    """ Compute the smallest knowledge space containing a famly of kstFrozensets

    Parameters
    ----------
    structure: set
        Family of kstFrozensets

    Returns
    -------
    Set of kstFrozensets
        Knowledge space

    Examples
    --------
    >>> from kstpy.data import xpl_basis
    >>> constr(xpl_basis)
    """
    for x in structure:
        if not isinstance(x, kstFrozenset):
            raise TypeError("structure must be a list or set of kstFrozenset's.")
    space = set({kstFrozenset({}), kstFrozenset(domain(structure))})
    space.union(structure)
    for state in structure:
        new_states = set({})
        for s in space:
            if not ((set({state | s})) <= space):
                new_states.add((state | s))
        space = space | new_states
    return space

def basis(structure):
    """ Determine the basis of a knolwdge space/structure
    
    Parameters
    ----------
    structure: set
        Family of kstFrozensets
    
    Returns
    -------

    Set of kstFrozensets
        Basis

    Examples
    --------
    >>> from kstpy.data import xpl_basis
    >>> s = constr(xpl_basis)
    >>> basis(s)
    """
    for x in structure:
        if not isinstance(x, kstFrozenset):
            raise TypeError("structure must be a list or set of kstFrozenset's.")
    b = set({})
    for state in structure:
        h = set(state)
        for i in structure:
            if set(i) < set(state):
                h = h - set(i)
            if h == set({}):
                break
        if len(h) > 0:
            b.add(kstFrozenset(state))
    return b

def surmiserelation(structure):
    """Compute the surmise relation for a knowledge structure
    
    Parameters
    ----------

    structure: set
        Family of kstFrozensets
    
    Returns
    -------

    Set of 2-tuples
        Surmise relation

    Examples
    --------
    >>> from kstpy.data import xpl_basis
    >>> s = constr(xpl_basis)
    >>> surmiserelation(s)

    """
    for x in structure:
        if not isinstance(x, kstFrozenset):
            raise TypeError("structure must be a list or set of kstFrozenset's.")
    d = domain(structure)
    sr = set({})
    b = basis(structure)

    for i in d:
        for j in d:
            sr.add((i,j))
    for s in b:
        for i in d:
            for j in d:
                if i in s and not j in s:
                    sr.discard((j,i))
                if j in s and not i in s:
                    sr.discard((i,j))
    return(sr)

def sr2basis(sr):
    """ Compute the basis corresponding to a surmise relation

    Parameters
    ----------

    sr: set (of 2-tuples)
        Surmise relation

    Returns
    -------

    Corresponding basis
        Set of kstFrozensets

    Examples
    --------
    >>> from kstpy.data import xpl_basis
    >>> sr = surmiserelation(xpl_basis)
    >>> b = sr2basis(sr)
    >>> print(xpl_basis, b)

    """
    if not isinstance(sr, set):
        raise TypeError("sr must be a set.")
    for x in sr:
        if not isinstance(x, tuple) or not len(x) == 2:
            raise TypeError("The elements of sr must be 2-tuples.")
    d = srdomain(sr)
    b = set({})
    for q in d:
        s = set({q})
        for p in sr:
            if p[1]==q:
                s.add(p[0])
        b.add(kstFrozenset(s))
    return b


def neighbourhood(state, structure, maxdist = 1):
    """
    Determine the neighbourhood of a state"

    Parameters
    ----------
    state: kstFrozenset
        State whose neighbourhood shall be determined
    structure: set (of kstFrozensets)
        Knowledge structure
    maxdist: int 
        Radius of the neighbourhood (default = 1)

    Returns
    -------

    Set containing the neighbourhood
        Set of kstFrozensets
 
    Examples
    --------
    >>> from kstpy.data import xpl_basis
    >>> from kstpy.helpers import kstFrozenset
    >>> s = constr(xpl_basis)
    >>> neighbourhood(kstFrozenset({"a"}), s)

   """
    if not isinstance(state, kstFrozenset):
        raise TypeError("state must be a kstFrozenset.")
    if not isinstance(structure, set):
        raise TypeError("structure must bed a set (of kstFrozenset's).")
    for x in structure:
        if not isinstance(x, kstFrozenset):
            raise TypeError("The elements of structure must be kstFrozenset's.")
    if not isinstance(maxdist, int):
        raise TypedEDrror("maxdist must be an integer number.")
    if not state in structure:
        raise ParameterMisfitError("The state is not contained in the structure.")
    n = set({})
    for s in structure:
        if (len(s ^ state) <= maxdist) & (s != state):
            n.add(s)
    return n

def fringe(state, structure, maxdist = 1):
    """
    Determine the inner, outer, and total fringe of a state"

    Parameters
    ----------
    state: kstFrozenset
        State whose fringe shall be determined
    structure: set (of kstFrozensets)
        Knowledge structure
    maxdist: int 
        Radius of the fringe (default = 1)

    Returns
    -------
    Fringe, inner fringe, and Outer fringe
        Dictionary of three sets: fringe, inner, and outer

    Examples
    --------
    >>> from kstpy.data import xpl_basis
    >>> from kstpy.helpers import kstFrozenset
    >>> s = constr(xpl_basis)
    >>> fringe(kstFrozenset({"a", "b"}), s, 2)

    """
    if not isinstance(state, kstFrozenset):
        raise TypeError("state must be a kstFrozenset.")
    if not isinstance(structure, set):
        raise TypeError("structure must bed a set (of kstFrozenset's).")
    for x in structure:
        if not isinstance(x, kstFrozenset):
            raise TypeError("The elements of structure must be kstFrozenset's.")
    if not isinstance(maxdist, int):
        raise TypedEDrror("maxdist must be an integer number.")
    if not state in structure:
        raise ParameterMisfitError("The state is not contained in the structure.")
    f = set({})
    fi = set({})
    fo = set({})
    n = neighbourhood(state, structure, maxdist)
    for s in n:
        f.add(s^state)
        if s.issubset(state):
            fi.add(s^state)
        elif state.issubset(s):
            fo.add(s^state)
    fl = {"fringe": f,
          "inner": fi,
          "outer": fo}
    return fl

def equivalence(structure):
    """Determine equivalence classes
    
    Parameters
    ----------

    structure: set of kstFrozensets
        Knowledge Structure

    Returns
    -------

    Equivalence classes
        Set of kstFrozensets

    Examples
    --------
    >>> from kstpy.data import xpl_basis
    >>> s = constr(xpl_basis)
    >>> equivalence(s)
    """
    if not isinstance(structure, set):
        raise TypeError("structure must bed a set (of kstFrozenset's).")
    for x in structure:
        if not isinstance(x, kstFrozenset):
            raise TypeError("The elements of structure must be kstFrozenset's.")
    d = domain(structure)
    ecl = set({})
    for q in d:
        c = set({q})
        for r in d:
            if q != r:
                cd = True
                for s in structure:
                    if len(set({q,r}) & set(s)) == 1:
                        cd = False
                if cd:
                    c.add(r)
        ecl.add(kstFrozenset(c))
    return ecl

                    
def gradations(s1, s2, structure):
    """Determine all gradations from s1 to s2 in structure
    
    Parameters
    ----------

    s1: kstFrozenset
        Starting state
    s2: kstFrozenset
        Goal state
    structure: set of kstFrozensets
        Knowledge Structure

    Returns
    -------
    All gradations from s1 to s2 within the structure
        Set of tuples of kstFrozensets
        
    Examples
    --------
    >>> from kstpy.data import xpl_basis
    >>> from kstpy.helpers import kstFrozenset
    >>> s = constr(xpl_basis)
    >>> gradations(kstFrozenset({"a"}), kstFrozenset({"a","b","c"}), s)
    """
    if not isinstance(s1, kstFrozenset):
        raise TypeError("s1 must be a kstFrozenset.")
    if not isinstance(s2, kstFrozenset):
        raise TypeError("s2 must be a kstFrozenset.")
    if not isinstance(structure, set):
        raise TypeError("structure must bed a set (of kstFrozenset's).")
    if not s1 in structure:
        raise ParameterMisfitError("s1 is not contained in structire.")
    if not s2 in structure:
        raise ParameterMisfitError("s2 is not contained in structire.")
    for x in structure:
        if not isinstance(x, kstFrozenset):
            raise TypeError("The elements of structure must be kstFrozenset's.")
    if s1 == s2:
        return set({tuple(set({s1}))})
    if not s1 < s2:
        return None
    res = set({})
    n = neighbourhood(s1, structure, maxdist=1)
    for s in n:
        if (s > s1) and (s <= s2):
            g = gradations(s, s2, structure)
            newg = set({})
            if (len(g) >= 1):
                for lp in g:
                    l = list(lp)
                    l.insert(0, s1)
                    lt = tuple(l)
                    newg = newg | set({lt})
                res = res | newg
    return(res)

    
    
def learningpaths(structure):
    """ Return all learning paths in a knwoledge structure
    
    Parameters
    ----------
    structure: set of kstFrozensets
        Knowledge structure

    Returns
    -------
    All learning paths in the structure, i.e. all gradations from the empty set to the full item set.
        Set of tuples of kstFrozensetsd
        
    Examples
    --------
    >>> from kstpy.data import xpl_basis
    >>> from kstpy.helpers import kstFrozenset
    >>> s = constr(xpl_basis)
    >>> learningpaths(s)
    """
    if not isinstance(structure, set):
        raise TypeError("structure must bed a set (of kstFrozenset's).")
    for x in structure:
        if not isinstance(x, kstFrozenset):
            raise TypeError("The elements of structure must be kstFrozenset's.")
    empty = kstFrozenset(set({}))
    Q = kstFrozenset(set(domain(structure)))
    return gradations(empty, Q, structure)


def trace(structure, newdomain):
    """Detrmin e the trace of the structure with the new domain

    Parameter
    ---------

    structure: set of kstFreozensets
        Knowledge structure
    newdomain: list (of items)
        Reduced domain

    Returns
    -------

    Reduced knowledge structure 
        Set of kstFrozensets
        
    Examples
    --------
    >>> from kstpy.data import xpl_basis
    >>> s = constr(xpl_basis)
    >>> trace(s, list(["a","b","c"]))
    """
    if not isinstance(structure, set):
        raise TypeError("structure must bed a set (of kstFrozenset's).")
    for x in structure:
        if not isinstance(x, kstFrozenset):
            raise TypeError("The elements of structure must be kstFrozenset's.")
    if not isinstance(newdomain, list):
        raise TypeError("newdomain must be a (sorted) list of items.")
    d = domain(structure)
    if not set(newdomain) < set(d):
        raise ParameterMisfitError("newdomain must be a strict subset of the domain of the structure!")
    t = set({})
    for s in structure:
        t.add(kstFrozenset(s & newdomain))
    return t
