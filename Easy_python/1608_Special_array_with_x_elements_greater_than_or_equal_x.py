class Solution:
    def specialArray(self, nums: List[int]) -> int:
        newnums=sorted(nums)
        for i in range(len(nums)+1):
            for j in range(len(newnums)):
                if newnums[j]>=i:
                    
                    if len(newnums)-j!=i:
                        break
                    else:
                        return i
        return -1
