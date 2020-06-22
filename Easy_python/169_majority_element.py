class Solution:
    import numpy as np
    def majorityElement(self, nums: List[int]) -> int:
        A=sorted(nums)
        return A[int(len(nums)/2)]
            
