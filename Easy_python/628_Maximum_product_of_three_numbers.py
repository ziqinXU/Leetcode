class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        A=sorted(nums)
        if A[1]>=0:
            return A[len(nums)-1]*A[len(nums)-2]*A[len(nums)-3]
        else:
            return max(A[len(nums)-1]*A[len(nums)-2]*A[len(nums)-3],A[len(nums)-1]*A[0]*A[1])
