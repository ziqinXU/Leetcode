///first attempt 100%faster, 100%less memory
//Idea:Pay attetion to leap year
class Solution {
public:
    int dayOfYear(string date) {
    vector<int>intdate;
    int first=0;
    intdate.push_back(stoi(date.substr(0,4)));//convert string into number
    intdate.push_back(stoi(date.substr(5,2)));
    intdate.push_back(stoi(date.substr(8,2)));
    int sum=0;
    int montharray[12]={31,28,31,30,31,30,31,31,30,31,30,31};
    for(int i=0;i<intdate[1]-1;i++)
    {
        sum=sum+montharray[i];
    }
    sum=sum+intdate[2];//all the days before
    if(intdate[1]>2&&((intdate[0]%400==0)||(intdate[0]%4==0&&intdate[0]%100!=0)))//leap year
    sum++;
    return sum;

    }
};
