///first attempt 45.06%faster, 25.00%less memory
//Idea:use queue to save nodes. Sort each row and return the largest one
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
    vector<int> largestValues(TreeNode* root) {
    vector<int> returnarray;
    if(root==NULL)
    return returnarray;
    vector<int>temp;
    queue<TreeNode*>queuearray;
    TreeNode* p=root;
    queuearray.push(p);
    TreeNode* first;
    TreeNode* last;
    
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
                
                //last=p->left;
                tempcount++;
            }
            if(p->right!=NULL)
            {
                queuearray.push(p->right);
                //last=p->right;
                tempcount++;
            }
            m--;
            temp.push_back(queuearray.front()->val);
            
            if(m==0)
            break;
            queuearray.pop();
            p=queuearray.front();
            
        }
        sort(temp.begin(),temp.end());
        returnarray.push_back(temp[temp.size()-1]);
        temp.clear();
        
        i++;
        
        count.push_back(tempcount);
        tempcount=0;
       
        //temp.push_back(queuearray.front()->val);
        queuearray.pop();
        p=queuearray.front();
        

    }

    return returnarray;
    }
};
