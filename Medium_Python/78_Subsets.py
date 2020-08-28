class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if len(nums)==0:
            return []
        res=[]
        templist=[]
        def backtrack(templist,k):
            res.append(templist[:])
            #print(templist)
            for i in range(k,len(nums)):
                templist=templist+[nums[i]]
                backtrack(templist,i+1)
                templist.pop()
        backtrack(templist,0)
        return res
