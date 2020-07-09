"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        res=[]
        if not root:
            return None
        else:
            def dfs(root):
                if not root:
                    return None
                else:
                    res.append(root.val)
                    for i in root.children:           
                        dfs(i)
        dfs(root)
        return res
