# LeetCode 283. Move Zeros

# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
# Note that you must do this in-place without making a copy of the array.

# Example 1:
# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]

# Example 2:
# Input: nums = [0]
# Output: [0]

"""
        Do not return anything, modify nums in-place instead.
        """
class Solution:
    def moveZeroes(self, nums):
        # Initialize pointers to left and right
        left = 0  # Represent a position to place a non-zero element
        right = 0  # Iterate through the array

        # Loop through the array using the right pointer
        while right < len(nums):
            # If the element at the right pointer is non-zero
            if nums[right] != 0:
                # Swap the non-zero element with the element at the left pointer
                nums[left], nums[right] = nums[right], nums[left]
                # Increment both pointers to continue the process
                left += 1
            # Move the right pointer to the next element in the array
            right += 1

solution = Solution()
nums = [0, 1, 0, 3, 12]
solution.moveZeroes(nums)
print(nums)
# Output: [1, 3, 12, 0, 0]
