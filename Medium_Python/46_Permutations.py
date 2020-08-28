#回溯，无需减枝
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums)==0:
            return []
        res=[]
        templist=[]
        def backtrack(res,templist,nums):
            if len(nums)==0:
                res.append(templist)
            #print(templist)
            for i in range(len(nums)):
                cur=nums[i]
                backtrack(res,templist+[cur],nums[:i]+nums[i+1:])
        backtrack(res,templist,nums)
        return res
