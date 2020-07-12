# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        res1=[]
        res2=[]
        if not root1:
            return None
        else:
            def dfs(root1):
                if not root1:
                    return None
                else:
                    if root1.left == None and root1.right==None:
                        res1.append(root1.val)
                    dfs(root1.left)
                    dfs(root1.right)
            dfs(root1)
        if not root2:
            return None
        else:
            def dfs(root2):
                if not root2:
                    return None
                else:
                    if root2.left == None and root2.right==None:
                        res2.append(root2.val)
                    dfs(root2.left)
                    dfs(root2.right)
            dfs(root2)
        if res1==res2:
            return True
        else:
            return False
        
                    
