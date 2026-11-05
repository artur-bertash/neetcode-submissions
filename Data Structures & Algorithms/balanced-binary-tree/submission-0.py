# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        memo = {}
        def depth(root):
            if not root:
                return 0
            if root in memo:
                return memo[root]
            memo[root] = 1 + max(depth(root.left), depth(root.right))
            return memo[root]
        if not -1 <= depth(root.left) - depth(root.right) <= 1:
            return False
        return True
            