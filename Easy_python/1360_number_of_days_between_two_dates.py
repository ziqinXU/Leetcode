class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        def checkdifference(year, month, day):
            totaldays=0
            for i in range(1971,year):
                if(i%400==0 or (i%4==0 and i%100!=0)):
                    totaldays=totaldays+366
                else:
                    totaldays=totaldays+365
            daysofmonth=[31,28,31,30,31,30,31,31,30,31,30,31]
            for i in range(0,month-1):
                totaldays=totaldays+daysofmonth[i]
            totaldays=totaldays+day
            if(month>2 and ((year%400==0) or (year%4==0 and year%100!=0))):
                totaldays=totaldays+1
            return totaldays
        year1 = int(date1[0:4])
        year2 = int(date2[0:4])
        month1 = int(date1[5:7])
        month2 = int(date2[5:7])
        day1 = int(date1[8:10])
        day2 = int(date2[8:10])
        return abs(checkdifference(year1, month1,day1)-checkdifference(year2, month2,day2))
