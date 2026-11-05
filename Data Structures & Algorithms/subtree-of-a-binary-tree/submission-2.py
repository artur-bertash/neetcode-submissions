# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        ids = {}

        def get_id(node): 
            if not node:
                return 0

            key = (node.val, get_id(node.left), get_id(node.right))

            if key not in ids:
                ids[key] = len(ids) + 1
            return ids[key]

        target = get_id(subRoot)
        found = False

        def search(node):
            nonlocal found
            if not node:
                return 0
            key = (node.val, search(node.left), search(node.right))
            if key not in ids:
                ids[key] = len(ids) + 1
            if ids[key] == target:
                found = True
            return ids[key]

        search(root)
        return found