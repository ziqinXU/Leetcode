# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getLonelyNodes(self, root: TreeNode) -> List[int]:
        res=[]
        if not root:
            return None
        else:
            def dfs(root):
                if not root:
                    return None
                if root:
                    if root.right is None and root.left is not None:
                        res.append(root.left.val)
                    elif root.left is None and root.right is not None:
                        res.append(root.right.val)
                    dfs(root.left)
                    dfs(root.right)
            dfs(root)
        return res
    
