# Divide and Conquer algorithm:
# Break down the problem into the multiple sub-problems recursively until they become simple to solve
# Solution are combined to solve original problem
# O(n*log(n))Optimal running time

# Running time: [ Depends heavily on how you pick the PIVOT ELEMENT ]
# O(n^2) worst case
# O(n* log(n)) best and average case

# GENERAL PRINCIPLE
# 1. Choose PIVOT element (Usually last or random)
# 2. Stores element less than PIVOT in left subarray
#    Stores element greater than PIVOT in right subarray
# 3. Call quicksort recursively on left subarray
#    Call quicksort recursively on right subarray
# this recursion will go on until the array size is 1 and when the array size of the subarray is 1,
# it is already sorted

def quicksort(arr, left, right):
    # passes three parameters, array, left and right indexes, left and right determines the part that need to be sort,
    # at the beginning, a whole array to be sorted. So, left will be 0, right will be the length of the array

    if left < right:  # checks left is less than right, which means subarray does contain at least two elements
        partition_arr = partition(arr, left, right)

        # call quicksort on all elements that are less than the pivot element
        quicksort(arr, left, partition_arr - 1)

        # call quicksort on subarray that contains all that are greater than the pivot element
        quicksort(arr, partition_arr + 1, right)


def partition(arr, left, right):
    # returns the index of the pivot element after the first step of quicksort
    i = left  # left point of the array to sort
    j = right - 1  # point right of the pivot
    pivot = arr[right]

    # i moves to the right and j moves to left until i and j cross
    while i < j:

        # i to the right,while I is not at the end of the array, and element at index i is less than pivot , increase i
        while i < right and arr[i] < pivot:
            i += 1

        # j is greater than left and the element at index j, is greater than pivot, decrease j because j moves to the
        # left
        while j > left and arr[j] >= pivot:
            j -= 1

        # both while loops are finish, check if those two elements crossed yet, if didn't,
        # implement swap at the index i with the element at index j
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    # after i and j crossed, array index is greater than pivot, do another swap with the index i and the next right
    if arr[i] > pivot:
        arr[i], arr[right] = arr[right], arr[i]

    # quick sort function define earlier needs the i to determine where to split the array to call quicksort recursilvely
    return i


arr = [22, 11, 88, 66, 55, 77, 33, 44]
quicksort(arr, 0, len(arr) - 1)  # left is 0 at the beginning, right is length of array-1
print(arr)
