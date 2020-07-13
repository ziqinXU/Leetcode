# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        flag=0
        if p is None and q is None:
            return True
        if p and q:
            def dfs(p,q,flag):
               
                if p is None and q is not None:
                    flag=1
                if p is not None and q is None:
                    flag=1
                if p and q:
                    if p.val!=q.val:
                        flag=1
                    flag=dfs(p.left,q.left,flag)
                    flag=dfs(p.right,q.right,flag)
                return flag
            flag=dfs(p,q,flag)
        else:
            return False
        if flag==0:
            return True
        else:
            return False
