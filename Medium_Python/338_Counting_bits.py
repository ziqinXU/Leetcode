class Solution:
    def countBits(self, num: int) -> List[int]:
        returnlist=[]
        for i in range(num+1):
            returnlist.append(list(bin(i)).count('1'))
        return returnlist
