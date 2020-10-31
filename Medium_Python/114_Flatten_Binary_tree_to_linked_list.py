# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        res=list()
        def preorder(root):
            if root:
                res.append(root)
                preorder(root.left)
                preorder(root.right)
        preorder(root)
        for i in range(1,len(res)):
            pre,cur=res[i-1],res[i]
            pre.right=cur
            pre.left=None
        return res
