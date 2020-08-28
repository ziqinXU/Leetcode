class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        trustarr=[0]*(N)
        for i in range(len(trust)):
            trustarr[trust[i][0]-1]=trustarr[trust[i][0]-1]-1
            trustarr[trust[i][1]-1]=trustarr[trust[i][1]-1]+1
        if max(trustarr)==N-1:
            return trustarr.index(N-1)+1
        else:
            return -1
