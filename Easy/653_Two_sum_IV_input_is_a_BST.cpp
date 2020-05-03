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
    void checkarray(TreeNode* root)
    {
        if(root)
        {
            checkarray(root->left);
            intarray.push_back(root->val);
            checkarray(root->right);
        }
    }
    bool findTarget(TreeNode* root, int k) {
        checkarray(root);
        int i=0,j=intarray.size()-1;
        while(i<j)
        {
            if(intarray[i]+intarray[j]==k)
            return true;
            if(intarray[i]+intarray[j]<k)
            {
                i++;
            }
            if(intarray[i]+intarray[j]>k)
            {
                j--;
            }
        }
        return false;

    }
};
