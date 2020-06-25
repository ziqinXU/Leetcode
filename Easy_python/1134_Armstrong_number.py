class Solution:
    def isArmstrong(self, N: int) -> bool:
        length=len(str(N))
        eachpos=list(str(N))
        listsum=0
        for i in range(len(eachpos)):
            listsum=listsum+pow(ord(eachpos[i])-ord('0'),length)
        if listsum==N:
            return True
        else:
            return False
