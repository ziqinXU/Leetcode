class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i=0
        while i< len(nums):
            if nums.index(nums[i])<i:
                del nums[i]
                i=i-1
            i=i+1
        return len(nums)
