# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None:
            return head
        old=head
        res=[]
        while old is not None:
            res.append(old.val)
            old=old.next
        old=head
        i=len(res)-1
        while old is not None:
            old.val=res[i]
            old=old.next
            i=i-1
        return head
        
