class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        count=Counter(nums)
        found=0
        returnlist=[]
        for i in count:
            if count[i]==1:
                found=found+1
                returnlist.append(i)
            if found==2:
                return returnlist
