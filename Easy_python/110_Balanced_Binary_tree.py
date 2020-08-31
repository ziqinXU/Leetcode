# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def maxdepth(root,maxval):
            if root is None:
                return 0
            if root:
                leftmaxval=maxdepth(root.left,maxval)
                rightmaxval=maxdepth(root.right,maxval)
                if abs(leftmaxval-rightmaxval)>1 or leftmaxval==-1 or rightmaxval==-1:#若遇到有不平衡情况，则之后均不平衡
                    maxval=-1
                else:
                    maxval=max(leftmaxval,rightmaxval)+1
                
            return maxval
        maxval=maxdepth(root,0)
        if maxval>=0:
            return True
        else:
            return False
