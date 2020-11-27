class Solution {
public:
    int countNumbersWithUniqueDigits(int n) {
        int res=0;
        //N=0,1;N=1,10;N=2,9*9,N=3,9*9*8;
        int ans[11]={9,9,8,7,6,5,4,3,2,1,0};
        for(int i=0; i <=n; i++)
        {
            if(i>=11)
            {
                res+=0;
                continue;
            }
            if(i==0)
            {
                res+=1;
            }
            if(i==1)
            {
                res+=10;
            }
            if(i>1)
            {
                int temp=1;
                for(int j=0;j<i;j++)
                {
                   temp*=ans[j];
                }
                res+=temp;
            }
            

        }
        if(n>=1)
        return --res;
        else
        return res;
    }
};
