class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        returnarray = []
        a = sum(nums)
        for i in reversed(range(len(nums))):
            returnarray.append(a)
            a=a-nums[i]
        return returnarray[::-1]
       
