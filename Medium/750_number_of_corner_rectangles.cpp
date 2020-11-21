class Solution {
public:
    int countCornerRectangles(vector<vector<int>>& grid) {
        //记录出现过2个顶点的位置，用排列组合最后结果。每一行进行更新
        vector<vector<int>> dp;
        for(int j=0;j<grid[0].size();j++)
        {
            vector<int>temp;
            for(int k=0;k<grid[0].size();k++)
            {
                temp.push_back(0);
            }
            dp.push_back(temp);
        }
        for(int i=0;i<grid.size();i++)
        {
            
            for(int j=0;j<grid[0].size()-1;j++)
            {
                for(int k=j+1;k<grid[0].size();k++)
                {
                    if(grid[i][j]==1&&grid[i][k]==1)
                    {
                        dp[k][j]++;
                    }
                   
                }
            }
        }
        int res=0;
        for(int j=0;j<grid[0].size();j++)
        {
            
            for(int k=0;k<grid[0].size();k++)
            {
               if(dp[j][k]>=1)
               {
                   res+=(dp[j][k])*(dp[j][k]-1)/2;
               }
            }
           
        }
        return res;
    }
};
