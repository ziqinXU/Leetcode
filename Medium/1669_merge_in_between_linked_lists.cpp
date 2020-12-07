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
    ListNode* mergeInBetween(ListNode* list1, int a, int b, ListNode* list2) {
        //先将list2末端指向bb+1，再将list1的a-1指向list2
        ListNode* newnode1 = list1;
        ListNode* newnode2 = list2;
        ListNode* tempnode;
        while(newnode1->val!=b)
        {
            newnode1 = newnode1->next;
        }
        while(newnode2->next!=nullptr)
        {
            newnode2 = newnode2->next;
        }
        newnode2->next = newnode1->next;
        ListNode* newnode1first = list1;
        while(newnode1first->next->val!=a)
        {
            newnode1first = newnode1first->next;
        }
        newnode1first->next = list2;
        return list1;
        
    }
};
