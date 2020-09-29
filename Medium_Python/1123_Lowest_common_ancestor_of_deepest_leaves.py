# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#若左子树高于右，则存在于左，否则在右
class Solution:
    def lcaDeepestLeaves(self, root: TreeNode) -> TreeNode:
        
        def dfs(root):
            if not root:
                return None,-1
            if root:
                rootl,lh=dfs(root.left)
                rootr,rh=dfs(root.right)
                if lh==rh:
                    return root,lh+1
                elif lh>rh:
                    return rootl,lh+1
                else:
                    return rootr,rh+1
        newroot,height=dfs(root)
        return newroot

