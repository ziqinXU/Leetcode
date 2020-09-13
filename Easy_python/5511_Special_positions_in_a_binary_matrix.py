class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        res=[]
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j]==1:
                    res.append([i,j])
        result=[1]*len(res)
        #print(res)
        for i in range(len(res)-1):
            for j in range(i+1,len(res)):
                #if result[i]==1:
                #print(i,j,res[i],res[j])
                if res[i][0]==res[j][0]:
                    result[i]=0
                    result[j]=0
                    #break
                if res[i][1]==res[j][1]:
                    result[i]=0
                    result[j]=0
                    #break
        #print(result)
        return sum(result)
