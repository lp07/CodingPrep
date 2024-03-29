# 278. First Bad Version
# You are a product manager and currently leading a team to develop a new product.
# Unfortunately, the latest version of your product fails the quality check.
# Since each version is developed based on the previous version, all the versions after a bad version are also bad.
# Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one,
# which causes all the following ones to be bad.
# You are given an API bool isBadVersion(version) which returns whether version is bad.
# Implement a function to find the first bad version. You should minimize the number of calls to the API.

# 1. Input: n = 5, bad = 4, Output: 4
# Explanation:
# call isBadVersion(3) -> false
# call isBadVersion(5) -> true
# call isBadVersion(4) -> true
# Then 4 is the first bad version.

# 2. Input: n = 1, bad = 1, Output: 1

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

def isBadVersion(version: int) -> bool:
    if version == 4:
        return True
    return False

class Solution:
    def firstBadVersion(self, n: int) -> int:
        low = 0
        high = n - 1
        while low <= high:
            mid = (low + high) // 2
            if isBadVersion(mid) == False:
                low = mid + 1
            else:
                high = mid - 1
        return low
solution = Solution()
n = 5
print(solution.firstBadVersion(n))
# Output: 4


