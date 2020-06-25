class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        A=sorted(items,reverse=True)
        number = A[0][0]
        returnarray=[]
        gradesum=0
        i=0
        while number>=1:
            count=0 
            while i<len(items) and A[i][0]==number and count<=4:
                gradesum=gradesum+A[i][1]
                i=i+1
                count=count+1
            averagesum=int(gradesum/5)
            returnarray.append([number,averagesum])
            number=number-1
            gradesum=0
            while i<len(A) and A[i][0]!=number:
                i=i+1
        return sorted(returnarray)
        

