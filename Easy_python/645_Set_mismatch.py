class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        returnarray=[0]*2
        A=Counter(nums)
        for i in range(1,len(nums)+1):
            if A[i]==0:
                returnarray[1]=i
            if A[i]==2:
                returnarray[0]=i
            if returnarray[1]!=0 and returnarray[0]!=0:
                return returnarray
