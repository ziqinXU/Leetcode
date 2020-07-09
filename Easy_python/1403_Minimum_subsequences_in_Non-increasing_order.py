class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        arrsum=sum(nums)
        tempsum=0
        returnlist=[]
        newarr=sorted(nums,reverse=True)
        for i in range(len(newarr)):
            tempsum=tempsum+newarr[i]
            returnlist.append(newarr[i])
            if tempsum>arrsum-tempsum:
                return returnlist
