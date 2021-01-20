/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* plusOne(ListNode* head) {
        ListNode* slow = new ListNode(0);
        slow->next = head;
        ListNode* fast = head;
        while(fast!=nullptr)
        {
            if(fast->val != 9)
            {
                slow = fast;
            }
            fast = fast ->next;
        }
        slow->val +=1;
        ListNode* cur = slow->next;
        while(cur!=nullptr)
        {
            cur->val = 0;
            cur = cur->next;
        }
        return slow->next == head? slow:head;
    }
};
