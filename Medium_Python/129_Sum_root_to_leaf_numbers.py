# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        returnarr=[]
        def dfs(templist,root):
            if root:
                if root.left is None and root.right is None:
                    #if templist not in returnarr:      
                    returnarr.append(templist+[root.val])
                        #print(returnarr)
                else:
                    #templist.append(root.val)
                    dfs(templist+[root.val],root.left)
                    dfs(templist+[root.val],root.right)
                    #templist.pop()
        dfs([],root)
        arrsum=0
        print(returnarr)
        for i in range(len(returnarr)):
            for j in range(len(returnarr[i])):
                arrsum+=returnarr[i][j]*pow(10,len(returnarr[i])-j-1)
        return arrsum
