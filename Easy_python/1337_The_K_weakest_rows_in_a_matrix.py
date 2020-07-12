class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        returnlist=[]
        for i in range(len(mat)):
            a=mat[i].count(1)
            b=i
            returnlist.append([a,b])
        returnlist=sorted(returnlist)
        arr=[]
        for i in range(len(mat)):
            arr.append(returnlist[i][1])
        return arr[:k]
