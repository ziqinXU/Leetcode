class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        totalsum=sum(nums)
        for i in range(0,len(nums)):
            if (totalsum-nums[i])%2==0:
                leftsum=sum(nums[0:i])
                rightsum=sum(nums[i+1:])
                if leftsum==rightsum:
                    return i
        return -1
