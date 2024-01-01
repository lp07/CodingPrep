# Two Sum II - Input array is sorted:
# Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a
# specific target number. You may assume that each input would have exactly one solution, and you may not use the
# same element twice

def two_sum_sorted(nums, target):
    left, right = 0,  len(nums) - 1

    while left < right:
        current_sum = nums[left] + nums[right]

        if current_sum == target:
            return [left + 1, right + 1] # adding 1, since we have added -1 index
        elif current_sum < target:
            left += 1
        else:
            right -= 1

    return None

sorted_nums = [2, 7, 11, 15]
target = 9
result = two_sum_sorted(sorted_nums, target)
print(result)  # Output: [1, 2] (because sorted_nums[1] + sorted_nums[2] == 9)