# 34. Find First and Last Position of Element in Sorted Array
# Given an array of integers nums sorted in non-decreasing order,
# find the starting and ending position of a given target value.
# If target is not found in the array, return [-1, -1].
# You must write an algorithm with O(log n) runtime complexity.
# Example 1:
# Input: nums = [5,7,7,8,8,10], target = 8, Output: [3,4]
# Example 2:
# Input: nums = [5,7,7,8,8,10], target = 6, Output: [-1,-1]
# Example 3:
# Input: nums = [], target = 0, Output: [-1,-1]

from typing import List
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binarySearchLeft(nums, target):
            low = 0
            high = len(nums) - 1
            while low <= high:
                mid = (low + high) // 2
                if target <= nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            return low

        def binarySearchRight(nums, target):
            low = 0
            high = len(nums) - 1
            while low <= high:
                mid = (low + high) // 2
                if target < nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            return high

        low_index = binarySearchLeft(nums, target)
        high_index = binarySearchRight(nums, target)

        if low_index <= high_index:
            return [low_index, high_index]
        else:
            return [-1, -1]

nums = [5, 7, 7, 8, 8, 10]
target = 8
solution = Solution()
result = solution.searchRange(nums, target)
print(result)

# Output; [3, 4]