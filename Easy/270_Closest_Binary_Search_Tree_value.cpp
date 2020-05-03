///first attempt 87.38%faster, 25%less memory
//Idea:Convert each node value into double type and compare with target value, if it is smaller than the last value, save
//the value and the current node value, return the node value at the end of the pre-order.
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
    double near=DBL_MAX;//maximum value of double
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
