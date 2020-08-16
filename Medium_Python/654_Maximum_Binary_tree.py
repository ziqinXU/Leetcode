# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#递归，依次选取当前数组中最大数，最大数左数组，最大数右数组。
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        if len(nums)==0:
            return None
        maxval=max(nums)
        index=nums.index(max(nums))
        root=TreeNode(maxval)#构建根
        root.left=self.constructMaximumBinaryTree(nums[0:index])
        root.right=self.constructMaximumBinaryTree(nums[index+1:])
        return root
