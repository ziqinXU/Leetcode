///first attempt 15.86%faster, 33.33%less memory
//Idea:in-order, already sorted, use two pointers to check the sum
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
    void checkarray(TreeNode* root)//in order recursive, save in an int array
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
            if(intarray[i]+intarray[j]==k)//if found, return true
            return true;
            if(intarray[i]+intarray[j]<k)//if lower than the sum, left pointer move one more right
            {
                i++;
            }
            if(intarray[i]+intarray[j]>k)//if bigger than the sum, right pointer move one more left
            {
                j--;
            }
        }
        return false;//not found

    }
};
