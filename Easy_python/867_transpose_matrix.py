class Solution:#按列取原A中元素，并转为新A中的行
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        newA=[]
        for i in range(len(A[0])):
            temp=[]
            for j in range(len(A)):
                temp.append(A[j][i])
            newA.append(temp)
        return newA
