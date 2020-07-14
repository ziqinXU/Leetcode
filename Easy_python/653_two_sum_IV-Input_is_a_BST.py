# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        res=[]
        if root:
            def dfs(root):
                if root:
                    
                    dfs(root.left)
                    res.append(root.val)
                    dfs(root.right)
            dfs(root)
        left=0
        right=len(res)-1
        while left<right:
            if res[left]+res[right]==k:
                return True
            elif res[left]+res[right]<k:
                left=left+1
            else:
                right=right-1
        return False
