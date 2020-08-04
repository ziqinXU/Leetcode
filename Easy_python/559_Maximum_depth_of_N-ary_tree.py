"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        if root.children:
            depth=[]
            for kid in root.children:
                depth.append(self.maxDepth(kid))
            return max(depth)+1
        else:
            return 1
        
                
