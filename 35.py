# 35. Search Insert Position
# Given a sorted array of distinct integers and a target value, return the index if the target is found.
# If not, return the index where it would be if it were inserted in order.
# You must write an algorithm with O(log n) runtime complexity.

# Input: nums = [1,3,5,6], target = 5, Output: 2
# Input: nums = [1,3,5,6], target = 2, Output: 1
# Input: nums = [1,3,5,6], target = 7, Output: 4

class Solution:
    def searchInsert(self, nums, target):
        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = (low + high) // 2
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                high = mid - 1
            elif target > nums[mid]:
                low = mid + 1
        return low

solution = Solution()
result = solution.searchInsert([1, 3, 5, 6], 2)
print(result)
# Output : 1
