# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        res=[]
        if root:
            def dfs(root):
                if root:
                    res.append(root.val)
                    dfs(root.left)
                    dfs(root.right)
            dfs(root)
        A=sorted(res)
        minval=10e10
        for i in range(len(A)-1):
            if A[i+1]-A[i]<minval:
                minval=A[i+1]-A[i]
        return minval
