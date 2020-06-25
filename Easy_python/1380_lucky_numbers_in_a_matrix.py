class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        #nested list use [row[1] for row in alist] to get columns
        colexpand=[]
        col=[]
        returnarray=[]
        for i in range(len(matrix)):
            colexpand.append([i,matrix[i].index(min(matrix[i]))])
            col.append(matrix[i].index(min(matrix[i])))
        for idx, number in enumerate(col):
            tempcol =[row[number] for row in matrix]
            if colexpand[idx][0]==tempcol.index(max(tempcol)):
                returnarray.append(matrix[colexpand[idx][0]][colexpand[idx][1]])
        return returnarray

        
        
