class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        if len(nums)<=1:
            return 0
        A=sorted(nums)
        if A[len(nums)-1]>=2*A[len(nums)-2]:
            return nums.index(A[len(nums)-1])
        else:
            return -1
