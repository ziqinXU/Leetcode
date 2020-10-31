# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.res=0
        def depth(root):
            if root is None:
                return 0
            if root:
                left=depth(root.left)
                right=depth(root.right)
                self.res=max(self.res,left+right)
                return max(left,right)+1
        depth(root)
        return self.res
