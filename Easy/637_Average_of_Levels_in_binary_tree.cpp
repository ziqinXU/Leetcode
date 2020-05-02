///first attempt 83.3%faster, 16.67%less memory
//Idea:Similar as task 107, only needs to be converted into double type and divided by number of elements in each level
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
    vector<double> averageOfLevels(TreeNode* root) {
    vector<double>averagenumber;
    vector<vector<double>>returnarray;
    if(root==NULL)//check whether the tree is empty
    return averagenumber;
    vector<double>temp;
    queue<TreeNode*>queuearray;
    TreeNode* p=root;
    queuearray.push(p);//push root into queue
    vector<double>count;//count number in each level
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
            temp.push_back((double)queuearray.front()->val);//count for current level
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

    for(int i=0;i<returnarray.size();i++)//can not use accumulate here, exceed the range. 
    {
         double sum=0;
        for(int j=0;j<returnarray[i].size();j++)
        {
            sum=sum+returnarray[i][j];
        }
        averagenumber.push_back(sum/count[i]);//average number of each level
        
    }
    return averagenumber;
    
    }
};
