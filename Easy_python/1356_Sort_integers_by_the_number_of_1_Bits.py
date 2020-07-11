class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        B=sorted(arr,key=lambda x:(str(bin(x)).count('1'),x))
        return B
