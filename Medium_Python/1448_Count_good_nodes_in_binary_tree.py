# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    import math
    
    def goodNodes(self, root: TreeNode) -> int:
        self.count=0
        def dfs(root,maxval):
            if root:
                #print(root.val)
                if root.val>=maxval:
                    maxval=root.val
                    self.count+=1
                dfs(root.left,maxval)
                dfs(root.right,maxval)
            
        maxval=-math.inf
        dfs(root,maxval)
        return self.count
