///first attempt 37.18%faster, 100%less memory
//Idea:use queue to get order in levels, push elements in the queue and let first element out if its left and right node 
//are visited. Exit the loop if all left and right node of current level are added to the queue. Move the pointer to the 
//first element of the next level, count the number of each level, save in vector.
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
    vector<vector<int>> levelOrderBottom(TreeNode* root) {
    vector<vector<int>>returnarray;
    if(root==NULL)//check whether the tree is empty
    return returnarray;
    vector<int>temp;
    queue<TreeNode*>queuearray;
    TreeNode* p=root;
    queuearray.push(p);//push root into queue
    TreeNode* first;
    TreeNode* last;    
    vector<int>count;//count number in each level
    int tempcount=0;
    count.push_back(1);
    int i=0;
    while(queuearray.size()>0)//if all nodes are visited, exit.
    {
        int m=count[i];    
        while(1)
        {      
            if(p->left!=NULL)//add left node if exists
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
            temp.push_back(queuearray.front()->val);//count for current level
            if(m==0)//if all nodes in current level are visited, exit.
            break;
            queuearray.pop(); //if its left and right nodes are added into queue, let current node out
            p=queuearray.front();
            
        }
        returnarray.push_back(temp);//add all elements from current level in
        temp.clear();    
        i++;   
        count.push_back(tempcount);//count number of nodes in current level
        tempcount=0;
        queuearray.pop();//let last element from current level out
        p=queuearray.front();
        

    }
    vector<int>tempexchange;
    for(int i=0;i<returnarray.size()/2;i++)//reverse order
    {
        tempexchange=returnarray[i];
        returnarray[i]=returnarray[returnarray.size()-1-i];
        returnarray[returnarray.size()-1-i]=tempexchange;
    }
    return returnarray;
    }
};
