# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        #快慢指针，快走2步，慢走一步
        fastpointer,slowpointer=head,head
        while fastpointer!=None and fastpointer.next!=None:
            fastpointer=fastpointer.next.next
            slowpointer=slowpointer.next
        return slowpointer
