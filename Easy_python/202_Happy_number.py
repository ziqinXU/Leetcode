class Solution:
    def isHappy(self, n: int) -> bool:
        visitedlist=[]
        number=n
        while True:
            currentsum=0
            while int(number/10)!=0:
                currentsum=currentsum+pow(number%10,2)
                number=int(number/10)
            currentsum=currentsum+pow(number%10,2)
            if currentsum in visitedlist:
                return False
            if currentsum==1:
                return True
            visitedlist.append(currentsum)
            number=currentsum

