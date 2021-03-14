class Solution {
public:
    int totalMoney(int n) {
        int day = n % 7;
        int week = n / 7;
        int res = 0;
        if(week >= 1)
        res += (28 * week + ((week-1)*7)*week/2);
        
        for(int i = 0; i < day; i++)
        {
            res += (week + i + 1);
        }
        return res;
    }
};
