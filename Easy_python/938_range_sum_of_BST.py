# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        res=[]
        if not root:
            return None
        else:
            def dfs(root):
                if root is None:
                    return None
                else:
                    if root.val>=L and root.val<=R:
                        res.append(root.val)
                    dfs(root.left)
                    dfs(root.right)
            dfs(root)
        return sum(res)
