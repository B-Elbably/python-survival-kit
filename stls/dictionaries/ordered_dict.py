"""
3- orderedDict
The order of keys is preserved as inserted (Python 3.6+ dict also does this natively)
Has some extra methods like move_to_end() , popitem()
More Memory consumption than normal dict
"""

print(" <==== OrderedDict ====> ")
from collections import OrderedDict

data = OrderedDict()
od = OrderedDict()
od["y"] = 2
od["z"] = 1
od["x"] = 3
od["a"] = 4
od["d"] = 5

# print("OrderedDict:", od)
# OrderedDict([('y', 2), ('z', 1), ('x', 3)])
print("Items in insertion order:\n")
for key, value in od.items():
    print(f"{key}: {value}")

# Move 'b' to end
od.move_to_end("z")
# Move 'a' to beginning
od.move_to_end("a", last=False)

print("\nAfter moving items:\n")
for key, value in od.items():
    print(f"{key}: {value}")


# Pop items
print("\nPopping items:\n")
last = od.popitem()
first = od.popitem(last=False)
print("first:", first)
print("last:", last)

print("\nAfter popping items:\n")
for key, value in od.items():
    print(f"{key}: {value}")


# Search about LRU Cache using OrderedDict
