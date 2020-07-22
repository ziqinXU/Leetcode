class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        A=sorted(nums)
        pos=[]
        for i in range(len(A)):
            if A[i]!=nums[i]:
                pos.append(i)
                break
        for j in reversed(range(i,len(A))):
            if A[j]!=nums[j]:
                pos.append(j)
                break
        if len(pos)==0:
            return 0
        else:
            return pos[1]-pos[0]+1
