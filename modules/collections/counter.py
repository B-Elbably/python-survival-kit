from collections import Counter

# Counter -> built-in frequency map
nums = [1, 2, 2, 3, 4, 4, 4]
counter = Counter(nums)
print("Counter: ", counter, '\n')


# update ? (you can loop and add manually also)
counter.update([3 , 5, 6])
counter.update({5: 1, 6: 1}) # or use dict
# counter += Counter(a = 2 , b = 3) # also works 
counter += {9:3}
print("Updated Counter: ", counter, '\n')

# most common k elements
most_common = counter.most_common(2) # top k frequent elements
print("Most common 2 elements: ", most_common, '\n')

# elements -> return all elements as per their frequency
elements = list(counter.elements())
print("Elements as per frequency: ", elements, '\n')

# subtract -> decrease frequency
counter.subtract([2, 4, 4])
counter -= {9: 3} # if value <= 0, it removes that key
print("After Subtracting [2, 4, 4]: ", counter, '\n')


"""
    Note: Counter is a subclass of dict
    Search for more methods like:
        - clear
        - copy
        - fromkeys
        - setdefault
"""
