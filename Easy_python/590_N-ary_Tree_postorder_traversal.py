"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        res=[]
        if not root:
            return None
        else:
            def dfs(root):
                if not root:
                    return None
                else:  
                    for i in root.children:           
                        dfs(i)
                    res.append(root.val)
        dfs(root)
        return res
