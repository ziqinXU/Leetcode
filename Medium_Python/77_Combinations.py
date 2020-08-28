#需要减枝，不走重复的路
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        if n==0:
            return []
        res=[]
        templist=[]
        nums=[x for x in range(1,n+1)]
        def backtrack(templist,p):
            if len(templist)==k:
                #print(templist)
                res.append(templist[:])
            #print(templist)
            for i in range(p,len(nums)):
                templist=templist+[nums[i]]
                backtrack(templist,i+1)
                templist.pop()
        backtrack(templist,0)
        return res
