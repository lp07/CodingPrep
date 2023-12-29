"""

Recursive binary search is a searching algorithm that divides a sorted array into halves and recursively searches
for a target element in one of the halves

Time Complexity:
Best Case: O(1)
Average Case: O(log N)
Worst Case: O(log N)

Space Complexity:
O(1), If the recursive call stack is considered then the auxiliary space will be O(logN).

"""

def recursive_binary_search(arr, target, low, high):
    if low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            return recursive_binary_search(arr, target, mid + 1, high)
        else:
            return recursive_binary_search(arr, target, low, mid - 1)
    else:
        return -1

my_sorted_array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target_element = 7

result = recursive_binary_search(my_sorted_array, target_element, 0, len(my_sorted_array) - 1)
print(result)
