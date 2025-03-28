# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.total = 0
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        # result = self.concat(root, "")
        self.concat(root)
        print(self.total)
        return self.total

    def concat(self, node, currentStr = "") -> str:
        if not node:
            return ""
        if not node.left and not node.right:
            self.total += int(currentStr + str(node.val)) 

        newString = currentStr + str(node.val)

        self.concat(node.left, newString) 
        self.concat(node.right, newString)
