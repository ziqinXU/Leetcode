class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        A=Counter(nums)
        arrsum=0
        for i in A:
            arrsum=arrsum+int(A[i]*(A[i]-1)/2)
        return arrsum
