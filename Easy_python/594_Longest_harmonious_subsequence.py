class Solution:
    def findLHS(self, nums: List[int]) -> int:
        arrset=sorted(list(set(nums)))
        lengthsum=0
        for i in range(len(arrset)-1):
            if arrset[i+1]-arrset[i]==1:
                tempsum=nums.count(arrset[i+1])+nums.count(arrset[i])
                if tempsum>lengthsum:
                    lengthsum=tempsum
        return lengthsum
