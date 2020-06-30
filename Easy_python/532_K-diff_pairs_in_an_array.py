class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        A=sorted(nums)
        returnset=[]
        for i in range(len(nums)):
            t=1
            while i+t < len(nums) and A[i+t]-A[i]<=k:
                if A[i+t]-A[i]==k:
                    returnset.append((A[i+t],A[i]))
                t=t+1

        return len(set(returnset))
