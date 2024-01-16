class Solution:
    def removeElement(self, nums, val):
        left = 0
        right = len(nums) - 1

        while left <= right:
            if nums[left] == val:
                # Swap nums[left] with nums[right]
                nums[left], nums[right] = nums[right], nums[left]
                right -= 1
            else:
                left += 1

        return left

solution = Solution()

nums1 = [3, 2, 2, 3]
val1 = 3
result1 = solution.removeElement(nums1, val1)
print(f"Output: {result1}, nums = {nums1[:result1] + ['_'] * (len(nums1) - result1)}")

nums2 = [0, 1, 2, 2, 3, 0, 4, 2]
val2 = 2
result2 = solution.removeElement(nums2, val2)
print(f"Output: {result2}, nums = {nums2[:result2] + ['_'] * (len(nums2) - result2)}")
