# 101. Symmetric Tree
# Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).
# Input: root = [1,2,2,3,4,4,3], Output: true
# Input: root = [1,2,2,null,3,null,3], Output: false

#  Definition for a binary tree node.

from typing import List, Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return False

        def isMirror(left:TreeNode, right:TreeNode) -> bool:

            # if both subtree are None, it is symmetric
            if left is None and right is None:
                return True
            # Only one subtree is None, it's not symmetric
            if left is None or right is None:
                return False
            # current nodes being compared by their value and their children node
            return left.val == right.val and isMirror(left.left, right.right) and isMirror(left.right, right.left)
        return isMirror(root.left, root.right)


root = TreeNode(1)
root.left = TreeNode(2, TreeNode(3), TreeNode(4))
root.right = TreeNode(2, TreeNode(3), TreeNode(4))
sol = Solution()
print(sol.isSymmetric(root))

# Output: False
