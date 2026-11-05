/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */

class Solution {
public:
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        p = (p->val < q->val) ? p : q;
        return dfs(root, p, q);
    }
    TreeNode* dfs(TreeNode* root, TreeNode *p, TreeNode *q) {
        if (!root) {
            return nullptr;
        }
        if (p->val <= root->val && root->val <= q->val){
            return root;
        }
        auto left = dfs(root->left, p, q);
        if (left) {
            return left; 
        }
        return dfs(root->right, p, q);
    }
};
