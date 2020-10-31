# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        dummyHead=ListNode(0)
        dummyHead.next=head
        temp=dummyHead

        while temp.next and temp.next.next:
            node1=temp.next
            node2=temp.next.next
            temp.next=node2#注意头节点下一个为node2
            node1.next=node2.next
            node2.next=node1
            temp=node1

        return dummyHead.next
