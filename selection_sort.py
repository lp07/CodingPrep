# Simple sorting algorithm
# Simple implementation
# Quadratic running time O(n^2) makes slower to compare more complex algorithm like merge sort

# GENERAL IDEA:
# find the minimum element and place it to the front
# sequentially build up the sorted list
# starting from first element, marked as a current minimum,
# iterate through a whole list in an inner loop to check the element is less that the current minimum
# if current minimum is greater than the element in a loop, swap and mark as a new current minimum

def selection_sort(arr):

    # loop for to find the minimum element from the list and place it at the first position at the list

    # index 0 from the list minus 1, skip the last index,
    # because selection sort arrives at this point it already is finish, as nothing to compare
    for i in range(0, len(arr) - 1):
        current_min = i

    # find the second-smallest element and place it at the second position in the list
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[current_min]:
                current_min = j

    # swap, assign the element at the current min index to the position i to position current minimum index
        arr[i], arr[current_min] = arr[current_min], arr[i]

arr = [2, 6, 5, 1, 3, 4]
selection_sort(arr)
print(arr)


