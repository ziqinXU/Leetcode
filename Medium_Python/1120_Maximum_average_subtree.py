# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maximumAverageSubtree(self, root: TreeNode) -> float:
        self.rootsum=[]
        self.count=[]
        self.average=[]
        def dfs(root):
            if not root:
                return 0,0
            if root:
                leftsum,leftcount=dfs(root.left)
                rightsum,rightcount=dfs(root.right)
                #self.rootsum.append(leftsum+rightsum+root.val)
                #self.count.append(leftcount+rightcount+1)
                self.average.append((leftsum+rightsum+root.val)/(leftcount+rightcount+1))
                return leftsum+rightsum+root.val,leftcount+rightcount+1
            
        dfs(root)
        return max(self.average)
