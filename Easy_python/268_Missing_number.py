class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        length=len(nums)
        nums=sorted(nums)
        if length not in nums:
            return length
        if 0 not in nums:
            return 0
        for i in range(len(nums)):
            if i!=nums[i]:
                return i
