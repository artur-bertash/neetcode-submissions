# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        st = [root] if root else []
        # flip it doing not left - right - root
        # but rather        root right left
        while st:
            cur = st.pop()
            res.append(cur.val)
            if cur.left: st.append(cur.left)
            if cur.right: st.append(cur.right)
        return res[::-1]

