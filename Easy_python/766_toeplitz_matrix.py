class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        i=len(matrix)-2
        while i>=0:
            temp=[]
            j=0
            k=i
            while j<len(matrix[0]) and k<len(matrix):
                temp.append(matrix[k][j])
                j=j+1
                k=k+1
            if len(list(set(temp)))!=1:
                return False
            i=i-1
        j=1
        while j<len(matrix[0]):
            temp=[]
            n=j
            i=0
            while n<len(matrix[0]) and i<len(matrix):
                temp.append(matrix[i][n])
                i=i+1
                n=n+1
            if len(list(set(temp)))!=1:
                return False
            j=j+1
        return True
