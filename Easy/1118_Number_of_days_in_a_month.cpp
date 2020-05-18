class Solution {
public:
    int numberOfDays(int Y, int M) {
    int a=0;
    switch(M)
    {
        case 1:
        a=31;
        break;
        case 2:
        a=28;
        break;
        case 3:
        a=31;
        break;
        case 4:
        a=30;
        break;
        case 5:
        a=31;
        break;
        case 6:
        a=30;
        break;
        case 7:
        a=31;
        break;
        case 8:
        a=31;
        break;
        case 9:
        a=30;
        break;
        case 10:
        a=31;
        break;
        case 11:
        a=30;
        break;
        case 12:
        a=31;
        break;
    }
    if(M==2&&((Y%4==0&&Y%100!=0)||(Y%400==0)))
    a=29;
    return a;

    }
};
