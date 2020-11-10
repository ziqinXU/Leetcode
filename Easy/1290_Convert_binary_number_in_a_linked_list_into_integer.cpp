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
    int getDecimalValue(ListNode* head) {
        ListNode* cur = head;
        int sum=0;
        int count=0;
        while (cur!=nullptr)
        {
            sum = sum*2 + cur->val; //反向二进制转十进制
            cur = cur->next;
        }
        return sum;
    }
};
