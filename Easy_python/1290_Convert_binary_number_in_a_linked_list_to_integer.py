# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        temp = head
        returnvalue = 0
        while(temp is not None):
            returnvalue = returnvalue*2 + temp.val
            temp = temp.next
        return returnvalue
