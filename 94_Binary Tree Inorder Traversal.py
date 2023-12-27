# Given the root of a binary tree, return the inorder traversal of its nodes' values.

# Example 1:
# Input: root = [1,null,2,3], Output: [1,3,2]

# Example 2:
# Input: root = [], Output: []

# Example 3:
# Input: root = [1], Output: [1]

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal(self, root):
        # Initialize an empty list to store the result
        res = []
        # Initialize a stack to iterate the traversal
        stack = []
        # Start from the root of a tree
        current = root

        # Perform until there are NO NODES to visit and STACK IS NOT empty
        while current or stack:
            # Traverse from the left most node and push onto the stack
            while current:
                stack.append(current)
                current = current.left

            # Pop a node from the stack, process it and move on to the right most child
            current = stack.pop()
            res.append(current.val)
            current = current.right
        # Return the final result list
        return res

tree = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
# Create an instance of the Solution class
solution = Solution()

# Call the inorderTraversal method and print the result
result = solution.inorderTraversal(tree)
print(result)




