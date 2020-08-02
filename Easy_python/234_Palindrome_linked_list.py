# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        p=head
        res=[]
        while p:
            res.append(p.val)
            p=p.next
        for i in range(len(res)//2):
            if res[i]!=res[len(res)-i-1]:
                return False
        return True
