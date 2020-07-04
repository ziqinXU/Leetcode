class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        A=Counter(nums)
        mode=0
        checklist=[]
        for i in A:
            if A[i]>mode:
                mode=A[i]
        for i in A:
            if A[i]==mode:
                checklist.append(i)
        minlen=1000000
        for i in range(len(checklist)):
            current=checklist[i]
            index1=nums.index(current)
            for j in reversed(range(len(nums))):
                if nums[j]==current:
                    index2=j
                    break
            if index2-index1+1<minlen:
                minlen=index2-index1+1
        return minlen
