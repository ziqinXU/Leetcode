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
    vector<vector<int>> zigzagLevelOrder(TreeNode* root) {
        //按层遍历，根据层数奇偶reverse返回
        vector<vector<int> > res;
        vector<TreeNode*> queue;     
        vector<int>len;
        int layernumber = -1;
        if(root != nullptr)
        {
            queue.push_back(root);
            
            len.push_back(1);
            
        }
        int t = 0;
        vector<int> count;
        count.push_back(1);
        int eachlayer;
        while(queue.size() > 0)
        {
            layernumber++;
            eachlayer = 0;
            int m=count[layernumber];
            vector<int> temp;
            while(m!=0)
            {
                TreeNode* cur = queue[0];
                if(cur->left!= nullptr)
                {
                    queue.push_back(cur->left);
                    
                    eachlayer++;
                }
                if(cur->right!= nullptr)
                {
                    queue.push_back(cur->right);
                    
                    eachlayer++;
                }
                temp.push_back(cur->val);      
                queue.erase(queue.begin());
                m--;    
            }
            if(layernumber%2==0)
            {
                res.push_back(temp);
            }
            else
            {
                std::reverse(temp.begin(),temp.end());
                res.push_back(temp);
            }
            temp.clear();
            count.push_back(eachlayer);   
        }
        return res;
    }
};
