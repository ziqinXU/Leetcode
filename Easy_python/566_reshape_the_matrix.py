class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        if len(nums[0])*len(nums)!=r*c:
            return nums
        else:
            res=[]
            returnlist=[]
            for i in range(len(nums)):
                res=res+nums[i]
            k=0
            for i in range(r):
                temp=[]
                for j in range(c):
                    temp.append(res[k])
                    k=k+1
                returnlist.append(temp)
            return returnlist
