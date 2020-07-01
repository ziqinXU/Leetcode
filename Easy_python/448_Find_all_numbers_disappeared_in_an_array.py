class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        A=Counter(nums)
        M=set(A)
        returnarray=[]
        for i in range(1,len(nums)+1):
            if i not in M:
                returnarray.append(i)
        return returnarray

        
        
