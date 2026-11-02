# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # in order means left - root - right
        st = []
        cur = root
        res = []
        while st or cur:
            while cur:
                st.append(cur)
                cur = cur.left
            
            node = st.pop()
            res.append(node.val)

            cur = node.right
        return res