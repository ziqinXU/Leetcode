# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
'''
官方解释
    如果当前节点有两个孩子，那我们在递归时，需要在两个孩子的结果外都加上一层括号；
    如果当前节点没有孩子，那我们不需要在节点后面加上任何括号；
    如果当前节点只有左孩子，那我们在递归时，只需要在左孩子的结果外加上一层括号，而不需要给右孩子加上任何括号；
    如果当前节点只有右孩子，那我们在递归时，需要先加上一层空的括号 () 表示左孩子为空，再对右孩子进行递归，并在结果外加上一层括号。
    '''
class Solution:
    
    def tree2str(self, t: TreeNode) -> str:
        def dfs(t,res):
            if t:
                if t.left==None and t.right==None:
                    res=res+str(t.val)
                    
                if t.left==None and t.right!=None:#不可省略左边的括号
                    res=res+str(t.val)+'('+')'+'('+dfs(t.right,res)+')'
                if t.left!=None and t.right==None:
                    res=res+str(t.val)+'('+dfs(t.left,res)+')'
                    
                if t.left!=None and t.right!=None:
                    res=res+str(t.val)+'('+dfs(t.left,res)+')'+'('+dfs(t.right,res)+')'
            return res
        res=""
        res = dfs(t,res)
        return res
