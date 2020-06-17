class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        t=0
        returnarray=[]
        for i in range(left,right+1):
            for idx,k in enumerate(list(str(i))):
                if k!='0':#k is char here
                    if i%int(k)!=0:
                        t=1
                        break
                if k=='0':
                    t=1
            if t==0:
                returnarray.append(i)
            t=0
        return returnarray
                
