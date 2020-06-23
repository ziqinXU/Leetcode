class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        A=Counter(arr)
        for i in A:
            if A[i]>int(len(arr)/4):
                return i
