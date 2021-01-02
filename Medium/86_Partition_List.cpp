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
    ListNode* partition(ListNode* head, int x) {
        ListNode* biglist = new ListNode(0);
        ListNode* smalllist = new ListNode(0);
        ListNode* small = smalllist;
        ListNode* big = biglist;
        ListNode* p = head;
        while(p != nullptr)
        {
            if(p->val < x)
            {
                small->next = p;
                small = small->next;
            }
            else
            {
                big->next = p;
                big = big->next;
            }
            p = p->next;
        }
        big->next = nullptr;
        small->next = biglist->next;
        return smalllist->next;

    }
};
