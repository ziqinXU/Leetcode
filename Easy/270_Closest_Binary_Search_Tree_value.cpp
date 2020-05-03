/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    double near=DBL_MAX;
    int result;
    int closestValue(TreeNode* root, double target) {
        if(root)
        {
            if(fabs((double)root->val-target)<near)
            {
                near=fabs((double)root->val-target);
                result=root->val;
            }
            closestValue(root->left, target);
            closestValue(root->right, target);
        }
        return result;
    }
};
