# 1- list unpacking example
print(" <==== List Unpacking ===>")
arr = [1, 2, 3]
a, b, c = arr  # unpacking
[x, y, z] = arr  # unpacking
print(a, b, c)
print(x, y, z)
print(*arr)  # unpacking with *


# 2- extended unpacking
print("\n <==== Extended Unpacking ===>")
arr2 = [1, 2, 3, 4, 5]
a, *b, c = arr2  # b gets the middle elements as a list
print(a, b, c)

# 3- Tuple Unpacking
print("\n <==== Tuple Unpacking ===>")
tup = (10, 20, 30)
x, y, z = tup
print(x, y, z)

# 4- Set Unpacking
print("\n <==== Set Unpacking ===>")
s = {100, 200, 300}
p, q, r = s  # order is not guaranteed
print(p, q, r)
print(*s)  # unpacking with *

# 5- Dictionary unpacking
print("\n <==== Dictionary Unpacking ===>")
dict1 = {'name': 'Alice', 'age': 30, 'city': 'New York'}
name, age, city = dict1.values()  # unpacking values
print(name, age, city)

def func(name, age, city):
    print(f"Name: {name}, Age: {age}, City: {city}")

func(**dict1)
# print(**dict1)  # Error

