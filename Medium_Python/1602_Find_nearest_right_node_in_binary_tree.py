# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findNearestRightNode(self, root: TreeNode, u: TreeNode) -> TreeNode:
        def Levelorder(root,flag):
            queue=[]
            queue.append(root)
            if root.val==u.val:#若当前根节点为所找节点，则返回Null
                return None
            while len(queue)>0:
                size=len(queue)
                while size!=0:#层次遍历
                    nodes=queue.pop(0)
                    left=nodes.left
                    right=nodes.right
                    
                    if left is not None :#用flag记录是否找到节点，若上一节点为所寻节点，则返回当前节点
                        if flag==1:
                            return left
                        if left.val==u.val:
                            flag=1
                        
                        queue.append(left)
                    if right is not None:
                        if flag==1:
                            return right
                        if right.val==u.val:
                            flag=1
                        queue.append(right)
                    size-=1
                if flag==1:#若遍历完当前层，找到节点，但未返回，则说明右侧节点为Null
                    return None
            return None#遍历完成，未找到右侧节点，返回Null
        return Levelorder(root,0)
