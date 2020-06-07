class Solution:
    def sumZero(self, n: int) -> List[int]:
        returnarray=[]
        if n%2==0:
            for i in range(1,int(n/2+1)):
                returnarray.append(i)
                returnarray.append(-i)
            return returnarray
        if n%2==1:
            returnarray.append(0)
            for i in range(1,int(n/2+1)):
                returnarray.append(i)
                returnarray.append(-i)
            return returnarray
