class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        i=0
        returnlist=[]
        while i < len(nums):
            j=i+1
            while j < len(nums) and nums[j]-nums[j-1]==1:
                j=j+1
            if j==i+1:
                returnlist.append(str(nums[i]))
            else:
                tempstring=str(nums[i])+'->'+str(nums[j-1])
                returnlist.append(tempstring)
            #print(j)
            i=j
        return returnlist
