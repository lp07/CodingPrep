# Simple sorting algorithm
# Simple implementation
# Quadratic running time O(n^2) makes slower to compare more complex algorithms.

def insertion_sort(arr):

    # loop from the second element to the last element, iterate through all unsorted items
    # index 1 to length of the array
    for i in range(1, len(arr)):
        j = i  # list to the left and checks if swap needed and stops if no need to swap

        # swapping condition
        # check if left neighbour is bigger than the current element
        while arr[j - 1] > arr[j] and j > 0:
            arr[j - 1], arr[j] = arr[j], arr[j-1]
            j -= 1

arr = [2, 6, 5, 1, 3, 4]
insertion_sort(arr)
print(arr)