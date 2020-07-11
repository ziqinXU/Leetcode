class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows==0:
            return []
        triangle=[[1]]
        for i in range(1,numRows):
            temp=[None]*(i+1)
            temp[0]=1
            for j in range(1,i):
                temp[j]=triangle[i-1][j-1]+triangle[i-1][j]
            temp[i]=1
            triangle.append(temp)
        return triangle
                
        
