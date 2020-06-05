class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        returnarray=[]
        for idx in range(0, len(nums), 2):
            currentnumber=nums[idx+1]
            times=nums[idx]
            returnarray.extend([currentnumber]*times)
        return returnarray
