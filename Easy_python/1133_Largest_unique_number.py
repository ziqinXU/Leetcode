class Solution:
    def largestUniqueNumber(self, A: List[int]) -> int:
        newarray=sorted(A,reverse=True)
        B=Counter(newarray)
        for i in range(len(newarray)):
            if B[newarray[i]]==1:
                return newarray[i]
        return -1
        
