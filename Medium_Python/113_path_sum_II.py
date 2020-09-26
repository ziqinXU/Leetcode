# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, total: int) -> List[List[int]]:
        res=[]
        def dfs(root,temparr,total):
            if root:
                if not root.left and not root.right:
                    
                    temparr+=[root.val]
                    
                    if sum(temparr)==total:
                        res.append(temparr)
                        
                        temparr=[] 
                    else:
                        
                        temparr=[]

            
                
                
                dfs(root.left,temparr+[root.val],total)
                dfs(root.right,temparr+[root.val],total)
        dfs(root,[],total)
        return res
