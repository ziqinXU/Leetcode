# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        p=head
        if not head:
            return None
        while p and p.val==val:
            p=p.next
            head=head.next

        while p and p.next:
            if p.next.val==val:
                p.next=p.next.next
            else:
                p=p.next
        return head
