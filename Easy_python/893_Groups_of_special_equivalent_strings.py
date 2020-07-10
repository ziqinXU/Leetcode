class Solution:
    def numSpecialEquivGroups(self, A: List[str]) -> int:
        #奇数偶数位分别排序，去重
        returnlist=[]
        for i in range(len(A)):
            first=A[i][0::2]
            first=sorted(first)
            first="".join(first)
            second=A[i][1::2]
            second=sorted(second)
            second="".join(second)
            returnlist.append(first+second)
        return len(list(set(returnlist)))

        
