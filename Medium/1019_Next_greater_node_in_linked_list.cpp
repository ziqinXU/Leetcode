/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    vector<int> nextLargerNodes(ListNode* head) {
        stack<pair<int,int>> arr;
        vector<int>res(10000,0);
        ListNode* p = head;
        int pos = 0;
        while(p!=nullptr)
        {
            if(arr.size()==0)
            {
                arr.push(make_pair(p->val,pos));
            }
            else
            {
                while(arr.size()>0 && p->val>arr.top().first)
                {
                    int position = arr.top().second;
                    arr.pop();
                    
                    res[position] = p->val;
                }
                arr.push(make_pair(p->val,pos));
            }
            pos++;
            p = p->next;
        }
        return vector<int>(res.begin(),res.begin()+pos);
    }
};
