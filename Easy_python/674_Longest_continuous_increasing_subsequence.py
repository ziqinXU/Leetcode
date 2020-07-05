class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        maxlen=0
        j=0
        while j!=len(nums):
            count=1
            for i in range(j,len(nums)-1):
                if nums[i+1]-nums[i]>=1:
                    count=count+1
                else:
                    break
            if count>maxlen:
                maxlen=count
            
            j=j+1
        return maxlen
