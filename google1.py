# Google interview question, Sep 2022
# Given an integer array group 1st with nth , 2nd with n-1, 3rd with n-2 and so on.
# Repeat the process until all groups are completed and return the final ans
# e.g Array: 1, 2, 3, 4, 5, 6, 7, 8
# 1st Group: 18, 27, 36, 45
# 2nd Group: 1845, 2736
# 3rd: 18452736 --> Answer.

def group(array):
    array = [str(a) for a in array]

    while len(array) > 1:
        result = []
        for i in range(len(array) // 2):
            start = array[i]
            end = array[-(i + 1)]
            result.append(start + end)
        array = result
    return array[0]
array = [1, 2, 3, 4, 5, 6, 7, 8]
result = group(array)
print(result)

# output: 18452736
