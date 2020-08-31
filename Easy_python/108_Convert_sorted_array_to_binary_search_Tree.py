#中序遍历，每次选择中间偏左数字作为节点
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        left,right = 0,len(nums)-1
        def dfs(left,right):
            if left>right:
                return None
            mid=(left+right)//2
            
            root=TreeNode(nums[mid])
            root.left = dfs(left,mid-1)
            root.right = dfs(mid+1,right)
            return root
        root=dfs(left,right)
        return root
        
