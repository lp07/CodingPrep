# array = [16, 12, 9, 19, 11, 8]
# APPROACH
# 1. Add the first k components together and save it to currentSum variable
# Because this is the first sum, it is also the current maximum; Thus, save it in the variable maximumSum
# 2. As the window size is k, we move the window one place to the right and compute the sum of the items in the window.
# 3. Add the maximum if the currentSum is greater than the MaximumSum, and repeat step 2.
# TC = O(N), run only one loop
def maxSum(array, k):

    # length of the array
    length = len(array)

    # length of the array must be greater than the window size
    if length < k:
        print("Invalid")
        return -1

    # sum of first k elements
    window_sum = sum(array[:k])
    maximum_sum = window_sum

    # remove the first element of previous window
    # and add the last element of the current window to calculate the sum of remaining window by

    for i in range(length - k):
        window_sum = window_sum - array[i] + array[i + k]
        maximum_sum = max(window_sum, maximum_sum)
    return maximum_sum

array = [16, 12, 9, 19, 11, 8]
k = 3
print(maxSum(array, k))



