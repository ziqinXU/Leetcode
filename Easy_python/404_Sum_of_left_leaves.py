# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        res=[]
        if root is None:
            return 0
        else:
            def dfs(root):
                if root:
                    if root.left is not None and root.left.left is None and root.left.right is None:
                        res.append(root.left.val)
                    dfs(root.left)
                    dfs(root.right)
            dfs(root)
        return sum(res)
