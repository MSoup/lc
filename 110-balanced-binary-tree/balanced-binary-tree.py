# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def find_depth(self, node):
        if not node:
            return 0

        leftDepth, rightDepth = self.find_depth(node.left), self.find_depth(node.right)

        if leftDepth == -1 or rightDepth == -1:
            return -1
        if abs(leftDepth - rightDepth) > 1:
            return -1

        # this line returns 1 + the max depth of our left and right children
        return max(leftDepth, rightDepth) + 1

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # Specification: A well-formed binary tree is said to be "height-balanced" if
        # (1) it is empty, or
        # (2) its left and right children are height-balanced and
        # the height of the left tree is within 1 of the height of the right tree.
        if not root:
            return True

        # if the difference between ANY depth is greater than 1 we return -1
        return self.find_depth(root) > -1
