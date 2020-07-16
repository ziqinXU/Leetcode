# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        res=[]
        if root:
            def dfs(root):
                if root:
                    res.append(root.val)
                    dfs(root.left)
                    dfs(root.right)
            dfs(root)
        ressort=sorted(res)
        j=0
        while j<len(ressort):
            if ressort[j]>res[0]:
                return ressort[j]
            j=j+1
        return -1
