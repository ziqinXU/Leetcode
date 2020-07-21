class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        numberlist=[str(i) for i in range(1,n+1)]
        numberlist=sorted(numberlist)
        return [int(numberlist[i]) for i in range(len(numberlist))]
