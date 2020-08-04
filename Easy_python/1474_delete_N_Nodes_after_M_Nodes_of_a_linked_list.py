# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
##添加dummy结点
class Solution:
    def deleteNodes(self, head: ListNode, m: int, n: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        p=dummy
        while p.next:
            km=0
            while p.next and km<m:
                p=p.next
                km=km+1
            kn=0
            while p.next and kn<n:
                p.next=p.next.next
                kn=kn+1
            
        return dummy.next
