
# st = {} empty dict, not set
st = set() # empty set

# adding elements
st.add(1)
# st.add(1) # no effect, 1 already in set

# removing elements
st.remove(1)
# st.remove(1) # KeyError, 1 not in set

# safely removing elements
st.discard(1) # no error if 1 not in set

# st.clear() # remove all elements


# magic methods (all update the set in place)
st |= {2, 3}  # union
st &= {3, 4}  # intersection
st -= {4}     # difference
st ^= {3, 5}  # symmetric difference

"""
    Magic in dict also (Try it yourself)
    There functions do the same as above magic methods (Search)
"""

"""
    set in Python is implemented using hash tables.
    Search about time complexity of set operations in Python
    Search about 'Collision' in Hash Tables. (Important concept)
"""