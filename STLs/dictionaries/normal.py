"""
    1- simple dict
"""
print(" <==== Simple Dict ====> ")

data = {} # dict not a set
data["name"] = "Belal"
data["age"] = 20

# ========================
print(data) # all items 
print(data["name"])
print(data["age"])
# print(data["technology"]) # KeyError (Key not found)

# To avoid KeyError Check if key exists
if "technology" in data:
    print(data["technology"])

# use get
print(data.get("technology" , "default"))




