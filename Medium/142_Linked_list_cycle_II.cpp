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
    ListNode *detectCycle(ListNode *head) {
        set<ListNode*> checkcycle;
        ListNode* p = head;
        while(p!=nullptr)
        {
            if(checkcycle.find(p)!=checkcycle.end())
            {
                return p;
            }
            else
            {
                checkcycle.insert(p); 
            }
            p = p->next;
        }
        return nullptr;
    }
};
