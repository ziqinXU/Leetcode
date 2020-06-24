class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        A=Counter(nums)
        for i in A:
            if A[i]>1:
                return True
        return False
