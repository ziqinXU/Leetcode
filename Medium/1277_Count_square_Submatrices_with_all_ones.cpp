class Solution {
public:
    int countSquares(vector<vector<int>>& matrix) {
        //当前为1时：边界上的为1，其余看上方和左边以及左上角dp最小值+1，所有dp相加。
        vector<vector<int>> dp;
        int res=0;
        for(int i=0;i<matrix.size();i++)
        {
            vector<int> temp;
            for(int j=0;j<matrix[0].size();j++)
            {
                temp.push_back(0);
            }
            dp.push_back(temp);
            temp.clear();
        }
        if(matrix[0][0]==1)
        {
            dp[0][0]=1;
            res+=1;
        }
        for(int i=1;i<matrix.size();i++)
        {
            if(matrix[i][0]==1)
            {
                dp[i][0]=1;
            }
            res+=dp[i][0];
        }
        for(int j=1;j<matrix[0].size();j++)
        {
            if(matrix[0][j]==1)
            {
                dp[0][j]=1;
            }
            res+=dp[0][j];
        }
        for(int i=1;i<matrix.size();i++)
        {
            for(int j=1;j<matrix[0].size();j++)
            {
                if(matrix[i][j]==1)
                {
                    dp[i][j]=min(dp[i-1][j],min(dp[i-1][j-1],dp[i][j-1]))+1;
                }
                res+=dp[i][j];
                
            }
        }
        return res;

    }
};
