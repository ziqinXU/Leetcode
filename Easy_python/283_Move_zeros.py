class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i=0
        p=0
        count=0
        while i < len(nums):
            if nums[i]==0:
                del nums[i]
                count=count+1
                i=i-1
            i=i+1
        while p<count:
            nums.append(0)
            p=p+1
        
