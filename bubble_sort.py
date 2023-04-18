def bubble_sort(arr):

    # loop through the array backwards from the last element to the second element
    for i in range(len(arr) - 1, 0, -1):

        # loop through the first element to the ith element
        for j in range(i):

            # check if the current element is greater than the next element
            if arr[j] > arr[j + 1]:

                # If so, swap the position of current element and next element
                cur_idx = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = cur_idx

arr = [5, 3, 8, 6, 7, 2]
bubble_sort(arr)
print(arr)