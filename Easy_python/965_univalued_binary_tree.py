# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        res=[]
        flag=0
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
        
        if len(list(set(res)))==1:
            return True
        else:
            return False
