# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSameTree(root, subRoot):
            if not root and not subRoot:
                return True
            if not root or not subRoot:
                return False
            if root.val != subRoot.val:
                return False
            
            return True and isSameTree(root.left, subRoot.left) and isSameTree(root.right, subRoot.right)
        if not root or not subRoot:
            return False
        if isSameTree(root, subRoot):
            return True
        return False or isSameTree(root.left, subRoot) or isSameTree(root.right, subRoot)