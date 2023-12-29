"""
Reverse the element of an array.
Parameter - arr: List of elements to be reversed
Returns - Reversed array
"""

def reversed_array(arr):
    return arr[::-1]

my_array = [1, 2, 3, 4, 5]
Reversed_array = reversed_array(my_array)
print(Reversed_array)

# op: [5, 4, 3, 2, 1]

"""
Reverse the parameters of a string
Parameter - s: string to be reversed
Returns - Reversed string
"""

def reversed_string(str):
    return str[::-1]

my_string = "Hello World!"
Reversed_string = reversed_string(my_string)
print(Reversed_string)

# op: !dlroW olleH


""" 
ITERATIVE WAY: 
1) Initialize start and end index to start = 0 and end = (len) - 1
2) In a loop, swap -> arr[start] with arr[end] and changes start and end as start = start + 1 and end = end - 1
"""

def reversed_list(array, start, end):
    while start < end:
        array[start], array[end] = array[end], array[start]
        start += 1
        end -= 1
    return array
array = [11, 12, 13, 14, 15]
Reversed_list = reversed_list(array, 0, 4)
print(Reversed_list)

# op: [15, 14, 13, 12, 11]
# Time Complexity: O(n)
# Space Complexity: O(1)

"""
RECURSIVE WAY:
1) Initialize start and end indexes as start = 0, end = n-1 
2) Swap arr[start] with arr[end] 
3) Recursively call reverse for rest of the array.
"""

def recursive_way(arr, start, end):
    # Base case: If start is greater than or equal to end, return the array as is
    if start >= end:
        return arr
    # Make a recursive call to reverse the remaining elements in the array
    # Return the result of the recursive call
    arr[start], arr[end] = arr[end], arr[start]
    return recursive_way(arr, start + 1, end - 1)

arr = [10, 20, 30, 40, 50]
Recursive_way = recursive_way(arr, 0, 4)
print(Recursive_way)

# op: [50, 40, 30, 20, 10]
# Time Complexity: O(n)
# Space Complexity: O(n)





