# Divide and Conquer algorithm:
# Break down the problem into the multiple sub-problems recursively until they become simple to solve
# Solution are combined to solve original problem
# O(n*log(n))Optimal running time

# GENERAL PRINCIPLE
# 1. Split array in halves
# 2. Call Merge Sort on each half to sort them recursively
# 3. Merge both sorted halves into one sorted array

def merge_sort(arr):  # define a function with function name merge sort and pass the argument as arr

    # first, the function does something if length of an array is greater than 1
    # if not, array is already sorted and nothing to do.
    if len(arr) > 1:

        # define the recursion part with defining with two sub-arrays

        left_arr = arr[:len(arr) // 2]
        # one (left array) is goes from the beginning of the original array to the middle point

        # another one (right array) right array goes from the middle point to the end of the array
        right_arr = arr[len(arr) // 2:]

        # call merge sort recursively on both of the arrays
        merge_sort(left_arr)
        merge_sort(right_arr)

        # implement the merge sort
        # compare the left most element of one array and left most element of another array
        i = 0  # track the left most element in left array
        j = 0  # track the left most element in right array
        k = 0  # tack of the index in the merged array

        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:  # left array is smaller than the right array at current indexes
                arr[k] = left_arr[i]  # can save the value of the left array, inside the merged array
                i += 1
                # k +=1
            else:  # right array is smaller than the left array at the current indexes or equal
                arr[k] = right_arr[j]
                j += 1
                # k +=1
            k += 1  # increment of k in every while loop

        while i < len(left_arr):  # i, is still smaller, because there is still element is missing from the left array
            # to transfer to the merged array
            arr[k] = left_arr[i]
            i += 1
            k += 1

        #  every element of the left arrays is already in sorted
        #  checking the elements for the right array, first check the element is not at the end of the right array
        #  assign in merged array

        while j < len(right_arr):
            arr[k] = right_arr[j]
            j += 1
            k += 1


arr_test = [2, 3, 5, 1, 7, 4, 4, 4, 2, 6, 0]
merge_sort(arr_test)
print(arr_test)
