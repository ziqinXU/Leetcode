class Solution:
    def dayOfYear(self, date: str) -> int:
        year=int(date[:4])
        month=int(date[5:7])
        day=int(date[8:10])
       
        arrsum=0
        montharray=[31,28,31,30,31,30,31,31,30,31,30,31]
        for i in range(month-1):
            arrsum=arrsum+montharray[i]

        arrsum=arrsum+day
        if month>2 and ((year%400==0) or (year%4==0 and year%100!=0)):
            arrsum=arrsum+1
        return arrsum
