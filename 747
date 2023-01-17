class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        len(nums) <= 2
        print(0)
        a = max(nums)
        aa = nums.index(a)
        print(aa)
        u = []
        g = 0
        for i in nums:
            if(i != a):
                u.append(i)
        if (len(u) != 0):
            g = max(u)
        if (a >= 2 * g):
            return aa
        return -1    
