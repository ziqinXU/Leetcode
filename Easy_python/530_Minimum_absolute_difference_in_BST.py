# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        res=[]
        if not root:
            return None
        else:
            def dfs(root):
                if not root:
                    return None
                else:
                    res.append(root.val)
                    dfs(root.left)
                    dfs(root.right)
            dfs(root)
        res=sorted(res)
        minval=10e8
        for i in range(0,len(res)-1):
            if res[i+1]-res[i]<minval:
                minval=res[i+1]-res[i]
        return minval
