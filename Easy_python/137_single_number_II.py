class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        A=Counter(nums)
        for i in A:
            if A[i]==1:
                return i
