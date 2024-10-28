# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        leftDepth, rightDepth = self.maxDepth(root.left), self.maxDepth(root.right)
        
        # this line returns 1 + the max depth of our left and right children
        return 1 + max(leftDepth, rightDepth)
