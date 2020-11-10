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
    void deleteNode(ListNode* node) {
        node->val=node->next->val;//替换当前节点为下个节点的值，并改变指针，变相挪走下一个节点。
        node->next=node->next->next;
    }
};
