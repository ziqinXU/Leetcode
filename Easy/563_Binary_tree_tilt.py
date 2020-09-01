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
    int res=0;
    int tilt(TreeNode* root)
    {
        if(root==NULL)
        return 0;
        int leftsum=tilt(root->left);
        int rightsum=tilt(root->right);
        res+=abs(leftsum-rightsum);
        return leftsum+rightsum+root->val;
    }
    int findTilt(TreeNode* root) {
        tilt(root);
        return res;
    }
    
};
