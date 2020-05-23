///first attempt 100%faster, 100%less memory
//Idea:Since the year is between 1971 and 2100, we can calculate the days difference between current date and 1971.1.1
class Solution {
public:
    int checkdifference(int year, int month, int day)//calculate the days difference between current date and 1971.1.1
    {
        int totaldays=0;
        for(int i=1971;i<year;i++)
    {
        if(i%400==0||(i%4==0&&i%100!=0))
        totaldays=totaldays+366;
        else
        totaldays=totaldays+365;
    }
    int daysofmonth[12]={31,28,31,30,31,30,31,31,30,31,30,31};
    for(int i=0;i<month-1;i++)
    {
        totaldays=totaldays+daysofmonth[i];
    }
    totaldays=totaldays+day;
    if(month>2&&((year%400==0)||(year%4==0&&year%100!=0)))
    totaldays++;
    return totaldays;
    }
    int daysBetweenDates(string date1, string date2) {

    int year1=stoi(date1.substr(0,4));
    int year2=stoi(date2.substr(0,4));
    int month1=stoi(date1.substr(5,2));
    int month2=stoi(date2.substr(5,2));
    int day1=stoi(date1.substr(8,2));
    int day2=stoi(date2.substr(8,2));
   
    return abs(checkdifference(year1, month1,day1)-checkdifference(year2, month2,day2));
   
    }
};
