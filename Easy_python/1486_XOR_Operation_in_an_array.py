
class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        newlist=range(start,start+(n-1)*2+1,2)
        result=start
        for i in range(1,len(newlist)):
            result=newlist[i]^result 
        return result
