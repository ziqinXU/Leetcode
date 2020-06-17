class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        arrsum=0
        for idx,x in enumerate(sorted(nums)):
            if idx%2==0:
                arrsum=arrsum+x
        return arrsum
