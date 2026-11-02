from collections import ChainMap

dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}

chain = ChainMap(dict1, dict2)

print(chain['a'])  # from dict1 → 1
print(chain['b'])  # found in dict1 first → 2
print(chain['c'])  # from dict2 → 4

print("\nMaps inside ChainMap:", chain.maps)
print("Keys in ChainMap:", list(chain.keys()))
print("Values in ChainMap:", list(chain.values()))

# ✅ new_child()
chain = chain.new_child({'a': 5})

print("\nAfter adding new child:", chain.maps)
print("Value of 'a' now:", chain['a'])  # 5 (from new child)
print("Parents in ChainMap:", chain.parents)

# ✅ new parents
dict3 = {'a': 6}
chain = ChainMap(*chain.maps, dict3)  # add to the end
print(chain['a'])  # 5 (from the first map)

chain = ChainMap(dict3, *chain.maps) # add to the front 
print(chain['a'])  # 6 (from dict3)
