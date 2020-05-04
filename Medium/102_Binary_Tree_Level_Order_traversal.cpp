///first attempt 88.47%faster, 100%less memory
//Idea:Use queue to save numbers in each level, similar as task 107.
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
    vector<vector<int>> levelOrder(TreeNode* root) {
    vector<vector<int>>returnarray;
    if(root==NULL)
    return returnarray;
    vector<int>temp;
    queue<TreeNode*>queuearray;
    TreeNode* p=root;
    queuearray.push(p);  
    vector<int>count;
    int tempcount=0;
    count.push_back(1);
    int i=0;
    while(queuearray.size()>0)
    {
        int m=count[i];
        
        while(1)
        {
            
            if(p->left!=NULL)
            {
                queuearray.push(p->left);
                tempcount++;
            }
            if(p->right!=NULL)
            {
                queuearray.push(p->right);
                tempcount++;
            }
            m--;
            temp.push_back(queuearray.front()->val);
            
            if(m==0)
            break;
            queuearray.pop();
            p=queuearray.front();
            
        }
        returnarray.push_back(temp);
        temp.clear();    
        i++;     
        count.push_back(tempcount);
        tempcount=0;
        queuearray.pop();
        p=queuearray.front();

    }

    return returnarray;
 
    }
};
