# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        # if no node, return null
        if not root:
            return root

        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)

        else:
            # found key
            # case 1: 1 child
            if not root.left:
                return root.right
            if not root.right:
                return root.left

            # case 2: 2 children
            # find min in right subtree
            tmp = self.find_min(root.right)
            # set root.val to this value
            root.val = tmp.val
            # remove duplicates
            root.right = self.deleteNode(root.right, root.val)

        return root

    def find_min(self, node):
        if not node.left:
            return node

        return self.find_min(node.left)

