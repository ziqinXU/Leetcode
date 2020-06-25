class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        A=Counter(arr)
        compareA=[]
        for i in A:
            compareA.append(A[i])
        if len(compareA)!=len(set(compareA)):
            return False
        else:
            return True

