# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.sol = []
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return self.sol
        self.inorderTraversal(root.left)
        self.sol.append(root.val)
        self.inorderTraversal(root.right)

        return self.sol