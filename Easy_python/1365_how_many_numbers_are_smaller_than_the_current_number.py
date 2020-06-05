class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        result=sorted(nums)
        return [result.index(number) for number in nums]
