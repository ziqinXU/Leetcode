class Solution:
    def addDigits(self, num: int) -> int:
        while len(str(num))>1:
            current=num
            numbersum=0
            while int(current/10)!=0:
                numbersum=current%10+numbersum
                current=int(current/10)
            numbersum=current%10+numbersum
            num=numbersum
            #print(num)
        return num
