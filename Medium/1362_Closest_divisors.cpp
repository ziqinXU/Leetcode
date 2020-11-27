class Solution {
public:
    vector<int> closestDivisors(int num) {
        int num1 = num + 1;
        int num2 = num + 2;
        vector<int> res;
        int factor1 = sqrt(num1);
        int factor2 = sqrt(num2);
        int diff1=0;
        int diff2=0;
        while(1)
        {
            
            if(num1%factor1==0)
                break;
            else
                factor1--;
        }
        diff1=abs(factor1-num1/factor1);
        res.push_back(factor1);
        res.push_back(num1/factor1);
        while(1)
        {
            
            if(num2%factor2==0)
                break;
            else
                factor2--;
        }
        diff2=abs(factor2-num2/factor2);
        if(diff2<diff1)
        {
            res[0]=factor2;
            res[1]=num2/factor2;
        }
        return  res;

    }
};
