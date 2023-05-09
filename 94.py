# Binary Tree Inorder Traversal
# Given the root of a binary tree, return the inorder traversal of its nodes value
# 1. Input: root = [1,null,2,3], Output: [1,3,2]
# 2. Input: root = [], Output: []
# 3. Input: root = [1], Output: [1]


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.right = right
#         self.left = left
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # if root is None, return empty list
        if not root:
            return []

        # create an empty list to store the inorder traversal
        result = []

        # if root is exists, go to the left node
        if root.left:
            result += self.inorderTraversal(root.left)
            # append current node's value to the result
            result.append(root.val)

        # go to the right node if it is exists
        if root.right:
            result += self.inorderTraversal(root.right)
        return result

    # if not root:
    # return []
    # return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)