"""
2- defaultdict
"""

print(" <==== DefaultDict ====> ")
from collections import defaultdict

data = defaultdict(str)  # [key : ""] by default
# Search about default for : (list , set , float , ..etc) and lambda
data["name"] = "Belal"
data["age"] = 20
print(data)  # all items
print(data["name"])
print(data["age"])
print(data["technology"])  # No KeyError , returns ""
