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
    vector<int> preorderTraversal(TreeNode* root) {
        stack<TreeNode*> rootstack;
        vector<int> res;
        if(root!=nullptr)
        {
            rootstack.push(root);
            while(!rootstack.empty())
            {
                TreeNode* cur = rootstack.top();
                rootstack.pop();
                res.push_back(cur->val);
                if(cur->right!=nullptr)
                rootstack.push(cur->right);
                if(cur->left!=nullptr)
                rootstack.push(cur->left);
            }
        }
        return res;
    }
};
