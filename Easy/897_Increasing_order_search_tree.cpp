///first attempt 100%faster, 100%less memory
//Idea:rearrange the tree in in-order and then create a new tree and insert nodes
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
    vector<int>intarray;
    void returninorder(TreeNode* root)//int array
    {
        if(root)
        {
            returninorder(root->left);
            intarray.push_back(root->val);
            returninorder(root->right);
        }
    }
    TreeNode* increasingBST(TreeNode* root) {//create new tree
        returninorder(root);
        TreeNode *ans = new TreeNode(intarray[0]),*cur=ans;
        for(int i=1;i<intarray.size();i++)
        {
            cur->right = new TreeNode(intarray[i]);//add values
            cur=cur->right;
        }
        return ans;
    }

};
