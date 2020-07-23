class Solution:
    def minMoves(self, nums: List[int]) -> int:
        #相当于每个数字减小为最小值
        return sum(nums)-min(nums)*len(nums)
