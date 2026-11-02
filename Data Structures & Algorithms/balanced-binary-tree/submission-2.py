# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    memo = {}
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        def depth(root):
            if not root:
                return 0
            if root in self.memo:
                return self.memo[root]
            self.memo[root] = 1 + max(depth(root.left), depth(root.right))
            return self.memo[root]
        diff = abs(depth(root.left) - depth(root.right))
        if not diff <= 1:
            return False
        left = self.isBalanced(root.left)
        right = self.isBalanced(root.right)
        return left and right
            