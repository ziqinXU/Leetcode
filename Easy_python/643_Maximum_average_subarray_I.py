class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        i=0
        current=sum(nums[:k])
        last=sum(nums[:k])
        while i+k<len(nums):
            tempsum=last-nums[i]+nums[i+k]
            if tempsum>current:
                current=tempsum
            i=i+1
            last=tempsum
        return current/k
