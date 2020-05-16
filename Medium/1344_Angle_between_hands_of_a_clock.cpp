///first attempt %faster, %less memory
//Idea:Calculate the angle mathematically with two different situations.
class Solution {
public:
    double angleClock(int hour, int minutes) {
        double number;
        if(hour==12)//two special occasions
        hour=0;
        if(minutes==0)
        {
            if(hour>6)
            return (double)(12-hour)/12*360;
            else
            return (double)hour/12*360;
        }
        
        if((int)((double)minutes/60*12)>hour)//if minutes is larger than hour number
        {
            number=((double)minutes/60*12-((double)hour+1)+1-(double)minutes/60)*360/12;
            if(number>180)
            number=360-number;
            return abs(number);
        }
        else
        {
            number=((double)hour-(double)minutes/60*12+(double)minutes/60)*360/12;
             if(number>180)
            number=360-number;
            return abs(number);
        }
    }
};
