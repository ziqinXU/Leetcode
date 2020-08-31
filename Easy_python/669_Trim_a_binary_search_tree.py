# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#
'''
如果根结点太小，根结点的左子树的所有结点只会更小，说明根结点及其左子树都应该剪掉，因此直接返回右子树的修剪结果。
如果根结点太大，根结点的右子树的所有结点只会更大，说明根结点及其右子树都应该剪掉，因此直接返回左子树的修剪结果。
如果根结点没问题，则递归地修剪左子结点和右子结点。
如果结点为空，说明无需修剪，直接返回空即可。

作者：tyanyonecancode
'''
class Solution:
    def trimBST(self, root: TreeNode, L: int, R: int) -> TreeNode:
        def trim(root,L,R):
            if root is None:
                return None
            if root.val<L:
                return trim(root.right,L,R)
            if root.val>R:
                return trim(root.left,L,R)
            root.left=trim(root.left,L,R)
            root.right=trim(root.right,L,R)
            return root
        root=trim(root,L,R)
        return root
