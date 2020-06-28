class Solution:
    def findRelativeRanks(self, nums: List[int]) -> List[str]:
        A=sorted(range(len(nums)),reverse=True ,key=lambda k: nums[k])
        nums[A[0]]="Gold Medal"
        if len(nums)==1:
            return nums
        nums[A[1]]="Silver Medal"
        if len(nums)==2:
            return nums
        nums[A[2]]="Bronze Medal"
        if len(nums)==3:
            return nums
        for i in range(3,len(nums)):
            nums[A[i]]=str(i+1)
        return nums
        
