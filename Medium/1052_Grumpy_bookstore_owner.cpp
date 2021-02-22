class Solution {
public:
    int maxSatisfied(vector<int>& customers, vector<int>& grumpy, int X) {
        int normal = 0;
        int additional = 0;
        for(int i = 0; i < grumpy.size(); i++)
        {
            if(grumpy[i] == 0)
            {
                normal += customers[i];
            }
        }

        if(customers.size() <= X)
        {
            for(int i = 0; i < customers.size(); i++)
            {
                if(grumpy[i] == 1)
                {
                    additional += customers[i];
                }
            }
            return additional + normal;
        }
        int maxval = 0;
        for(int i = 0; i < X; i++)
        {
            if(grumpy[i] == 1)
            {
                additional += customers[i];
            }
            if(additional>maxval)
            maxval = additional;
        }
        
        for(int i = 1; i < grumpy.size()-X+1;i++)
        {
            if(grumpy[i-1]==1)
            {
                additional-=customers[i-1];
                //滑动窗口减去左边若为生气的状态
            }
            
            if(grumpy[i+X-1]==1)
            {
                additional+=customers[i+X-1];
                //滑动窗口添加右边若为生气的状态
            }
            if(additional>maxval)
            maxval = additional;
        }
        return maxval+normal;
    }
};
