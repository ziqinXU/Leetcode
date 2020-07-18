class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        newlist=sorted(nums)
        nums[::2]=newlist[:int(len(nums)/2)+len(nums)%2]
        nums[1::2]=newlist[int(len(nums)/2)+len(nums)%2:]
