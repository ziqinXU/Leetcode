class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxlen=0
        i=0
        while i <len(nums):
            count=0
            while i< len(nums) and nums[i]==1:
                count=count+1
                i=i+1
            if count>maxlen:
                maxlen=count
            i=i+1
        return maxlen
