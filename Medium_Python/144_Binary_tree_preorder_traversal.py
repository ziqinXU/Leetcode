# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        res=[]
        def preorderTraversalHelper(root):
            if root:
                res.append(root.val)
                preorderTraversalHelper(root.left)
                preorderTraversalHelper(root.right)

        preorderTraversalHelper(root)
        return res
