# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import numpy as np
from scipy import stats
class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        dicttree={}
        maxlen=0
        if root:
            def BST(root):
                if root:
                    if root.val in dicttree:
                        dicttree[root.val]=dicttree[root.val]+1
                    else:
                        dicttree[root.val]=1
                    BST(root.left)
                    BST(root.right)
            BST(root)
        for i in dicttree:
            if dicttree[i]>maxlen:
                maxlen=dicttree[i]
        return [x for x in dicttree if dicttree[x]==maxlen]
        
