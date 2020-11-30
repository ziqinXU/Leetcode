class Solution {
public:
    
    int minSteps(int n) {
        if(n==1)
        return 0;
        int res = 0;
        int i=2;
        int number=n,flag=0;
        while(i<=number/2+1)
        {
            while(n%i==0)
            {
                flag=1;
                n=n/i;
                
                res+=i;
            }
            i++;
        }
        if(flag==0)
        {
            return number;
        }
        else
        return res;
    }
};
