class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        A=sorted(nums)
        for i in range(0,len(A),2):
            if i+1<len(A) and A[i]!=A[i+1]:
                return A[i]
        return A[i]
        
