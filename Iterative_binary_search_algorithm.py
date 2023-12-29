"""
Perform binary search on a sorted array to find the target element.

    Parameters:
    - arr: Sorted list of elements to search through.
    - target: Element to search for.

    Returns:
    - Index of the target element if found, else -1.

    Iterative Binary Search:

In iterative binary search, a while loop is typically used to repeatedly divide the search space until the target
element is found or the search space is empty.
It uses two pointers, low and high, to define the current search space.
The loop continues until low is greater than high.
During each iteration of the loop, the middle element (mid) of the current search space is calculated.
If the target is equal to arr[mid], the search is successful.
If the target is less than arr[mid], the search continues in the left half, otherwise in the right half.

Time Complexity: O(log N)
Auxiliary Space: O(1)

"""

def binarySearch(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid  # return the index of a target is found
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

sorted_array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 7

result = binarySearch(sorted_array, target)
print(result)

