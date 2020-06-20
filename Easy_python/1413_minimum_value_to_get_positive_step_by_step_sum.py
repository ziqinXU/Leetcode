class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        minsum=0
        currentsum=0
        for idx, number in enumerate(nums):
            currentsum=currentsum+number
            if currentsum<minsum:
                minsum=currentsum
        return abs(minsum)+1
