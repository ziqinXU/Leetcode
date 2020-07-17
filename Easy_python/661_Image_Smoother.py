class Solution:
    def imageSmoother(self, M: List[List[int]]) -> List[List[int]]:
        returnlist=[]
        for i in range(len(M)):
            templist=[]
            for j in range(len(M[0])):
                up=max(i-1,0)
                down=min(i+1,len(M)-1)
                left=max(j-1,0)
                right=min(j+1,len(M[0])-1)
                arrsum=0
                for k in range(up,down+1):
                    arrsum=arrsum+sum(M[k][left:right+1])
                templist.append(int(arrsum/((right-left+1)*(down-up+1))))
            returnlist.append(templist)
        return returnlist
                
