# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findFrequentTreeSum(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        hashmap={}
        def dfs(root):
            if not root:
                return 0
            if root:
                prel=dfs(root.left)
                prer=dfs(root.right)
                if prel+prer+root.val not in hashmap:
                    hashmap[prel+prer+root.val]=1
                else:
                    hashmap[prel+prer+root.val]+=1
                return prel+prer+root.val    
        pre=dfs(root)
        
        hashmap=sorted(hashmap.items(), key=lambda x: x[1],reverse=True)
        res=[]
        
        maxval=hashmap[0][1]
        for i in range(len(hashmap)):
            if hashmap[i][1]==maxval:
                res.append(hashmap[i][0])
            
        return res
