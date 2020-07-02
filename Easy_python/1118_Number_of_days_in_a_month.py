class Solution:
    def numberOfDays(self, Y: int, M: int) -> int:
        days1=[1,3,5,7,8,10,12]
        days2=[4,6,9,11]
        if M in days1:
            return 31
        if M in days2:
            return 30
        if(M==2 and ((Y%4==0 and Y%100!=0) or (Y%400==0))):
            return 29
        else:
            return 28
