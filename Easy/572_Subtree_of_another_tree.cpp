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
    bool SameTree(TreeNode* s, TreeNode* t)
    {
        if(s==nullptr&&t==nullptr)
        {
            return true;
        }
        if(s==nullptr || t==nullptr)
        return false;
        if(s->val != t->val)
        return false;
        return SameTree(s->left,t->left) && SameTree(s->right,t->right);
      
    }
    bool isSubtree(TreeNode* s, TreeNode* t) {
        if(t==nullptr)
        return true;
        if(s==nullptr)
        return false;
        return isSubtree(s->left, t) || SameTree(s, t) || isSubtree(s->right, t);
    }
};
