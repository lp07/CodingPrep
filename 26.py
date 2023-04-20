class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        # brute-force approach
        # time complexity: O(n^2)
        # because each element is compared with the other element to check for duplicates.
        # i = 0
        # while i < len(nums) - 1:
        # if nums[i] == nums[i + 1]:
        # nums.pop(i + 1)
        # else:
        # i += 1
        # return len(nums)

        # T.C = O(n)
        # input length is empty, return 0
        if len(nums) == 0:
            return 0
        # initialize a pointer at i, to track the element
        i = 0
        # loop through the list starting at i + 1 with pointer j
        for j in range(i + 1, len(nums)):
            if nums[j] != nums[i]:  # if element at j is different from the element at i
                i += 1  # increment i and set i to nums[j]
                nums[j] = nums[i]
        return [i + 1]  # return length of the new list, since i, is zero-indexed
