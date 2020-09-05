# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#从根节点开始遍历树
#如果节点 ppp 和节点 qqq 都在右子树上，那么以右孩子为根节点继续 1 的操作
#如果节点 ppp 和节点 qqq 都在左子树上，那么以左孩子为根节点继续 1 的操作
#如果条件 2 和条件 3 都不成立，这就意味着我们已经找到节 ppp 和节点 qqq 的 LCA 了
#作者：LeetCode

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def findcommon(root,p,q):
            if root:
                
                if p.val<root.val and q.val< root.val:
                    return findcommon(root.left,p,q)
                elif p.val>root.val and q.val>root.val:
                    return findcommon(root.right,p,q)
                else:
                    return root
        root = findcommon(root,p,q)
        return root
