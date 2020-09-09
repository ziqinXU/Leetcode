# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#两个指针分别遍历左右，当节点相同时，遍历左右子树
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None:
            return True
        def check(p:TreeNode,q:TreeNode):
            if p is None and q is None:
                return True
            if p is None or q is None:
                return False
            if p.val==q.val:
                return check(p.left,q.right) and check(p.right,q.left)

        return check(root.left,root.right) 
