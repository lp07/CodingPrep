# 1351. Count Negative Numbers in a Sorted Matrix
# Given a m x n matrix grid which is sorted in non-increasing order both row-wise and column-wise,
# return the number of negative numbers in grid.
# Input: grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]], Output: 8
# Explanation: There are 8 negatives number in the matrix.
# Input: grid = [[3,2],[1,0]], Output: 0

# Brute Force (TC: O(m*n) Iterate over each element of the matrix, SC: O(1) No additional space:
# count = 0
# for row in grid:
#     for element in row:
#         if element < 0:
#             count += 1
# return count

# Binary Search, for each row O(log n), here m rows TC: O(m log n), SC: O(1)
# count = 0
# n = len(grid[0])
# for row in grid:
#     low, high = 0, n - 1
#     while low <= high:
#     mid = (low + high) // 2
#         if row[mid] < 0:
#             high = mid - 1
#         else:
#             low = mid + 1
#     count += (n - low)
# return count


class Solution:
    def countNegetives(self, grid):
        count = 0
        n = len(grid[0])
        currentNegetive = n - 1  # rightmost column

        for row in grid:
            while currentNegetive >= 0 and row[currentNegetive] < 0:
                currentNegetive -= 1  # move to the left to searching for negative values
            count += (n - (currentNegetive + 1))
        return count


solution = Solution()
result = solution.countNegetives([[4, 3, 2, -1], [3, 2, 1, -1], [1, 1, -1, -2], [-1, -1, -2, -3]])
print(result)
