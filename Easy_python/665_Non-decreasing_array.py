class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        count=0
        pos=0
        for i in range(len(nums)-1):
            if nums[i]>nums[i+1]:
                count=count+1
                pos=i
            if count>1:
                return False
        if pos==0 or pos==len(nums)-2:
            return True
        if (pos+2<len(nums) and nums[pos]<=nums[pos+2]) or (pos-1>=0 and nums[pos-1]<=nums[pos+1]):
            return True
        else:
            return False
