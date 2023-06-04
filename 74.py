# 74. Search a 2D Matrix
# You are given an m x n integer matrix with the following two properties:
# Each row is sorted in non-decreasing order.
# The first integer of each row is greater than the last integer of the previous row.
# Given an integer target, return true if target is in matrix or false otherwise.
# You must write a solution in O(log(m * n)) time complexity.
# Example 1:
# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3, Output: true
# Example 2:
# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13, Output: false

class Solution:
    def searchMatrix(self, matrix, target):
        m = len(matrix)  # number of rows in the matrix
        n = len(matrix[0]) # number of columns in the matrix

        low = 0
        high = m*n - 1

        while low <= high:
            mid = (low + high) // 2

            # convert mid as an indexes of the matrix
            row = mid // 2
            col = mid % 2

            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                low = mid + 1
            else:
                high = mid - 1
        return False

solution = Solution()
result = solution.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13)
print(result)

# output: False
