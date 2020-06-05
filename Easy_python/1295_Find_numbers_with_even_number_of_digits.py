class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count=0;
        for number in nums:
            if len(str(number))%2==0:
                count=count+1
        return count
