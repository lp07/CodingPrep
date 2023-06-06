# Index of the first peak element(larger than its neighbours) appears in array
# nums = [1,2,1,3,5,6,4]

class Solution:
    def firstPeakElement(self, nums):
        if nums[0] > nums[1]:
            return nums[0]
        for i in range(0, len(nums) - 1):
            if nums[i] > nums[i - 1] and nums[i] > nums[i + 1]:
                return i
        return -1

solution = Solution()
result = solution.firstPeakElement([1, 2, 1, 3, 5, 6, 4])
print(result)

# output: 1