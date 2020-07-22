class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        factorlist=[]
        if num==1 or num<=0:
            return False
        for i in range(2,int(sqrt(num))+1):
            if num%i==0:
                factorlist.append(i)
                factorlist.append(int(num/i))
        factorlist.append(1)
        if sum(factorlist)==num:
            return True
        else:
            return False
