class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        totaldays=0
        weekday=0
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
        weekday=((totaldays-1)%7+5)%7
        weekdays=["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
        return weekdays[weekday]
