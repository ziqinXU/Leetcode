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
    int totalval=0;
    TreeNode* bstToGst(TreeNode* root) {
        //反向中序遍历，从右子树开始，用totoalval记录当前和，并赋值给当前节点。
        if(root!=nullptr)
        {
            bstToGst(root->right);
            totalval+=root->val;
            root->val=totalval;
            bstToGst(root->left);
        }
        return root;
    }
};
