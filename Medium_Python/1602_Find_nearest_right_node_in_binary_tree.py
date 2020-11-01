# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findNearestRightNode(self, root: TreeNode, u: TreeNode) -> TreeNode:
        res=[]
        def Levelorder(root,flag):
            queue=[]
            #seen=set()
            queue.append(root)
            res.append(root.val)
            if root.val==u.val:
                return None
            while len(queue)>0:
                size=len(queue)
                while size!=0:
                    nodes=queue.pop(0)
                    left=nodes.left
                    right=nodes.right
                    
                    if left is not None :
                        if flag==1:
                            return left
                        if left.val==u.val:
                            flag=1
                        
                        queue.append(left)
                        #seen.add(left.val)
                        res.append(left.val)
                    
                    if right is not None:
                        if flag==1:
                            return right
                        if right.val==u.val:
                            flag=1
                        queue.append(right)
                        #seen.add(right.val)
                        res.append(right.val)
                    size-=1
                if flag==1:
                    return None
            return None
        return Levelorder(root,0)
