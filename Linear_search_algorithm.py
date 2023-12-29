# Implementation of Linear Search Algorithm

"""
Perform linear search on given array to find the target element

Parameters:
    - arr: List of elements to search through
    - target: Element to search for.

Returns:
    - Index of the target element if found, else -1
"""

def liner_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Return the index of the target is found
    return -1  # return -1 if target is not found in the array

my_array = [4, 2, 7, 1, 9, 5]
target_element = 1
result = liner_search(my_array, target_element)
print(result)





