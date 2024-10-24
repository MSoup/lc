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
            # found the node we want to remove
            # if this node is a child, return the other sibling
            if not root.left:
                return root.right
            if not root.right:
                return root.left
            
            # get min of right subtree
            tmp = self.find_min(root.right)
            # assign root that we want to delete to min
            root.val = tmp.val
            # remove duplicate recursively
            root.right = self.deleteNode(root.right, root.val)
        
        return root

    def find_min(self, node):
        if not node.left:
            return node
        return self.find_min(node.left)