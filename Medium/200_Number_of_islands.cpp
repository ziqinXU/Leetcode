class Solution {
public:
    //深度优先搜索
    void dfs(vector<vector<char>>& grid,int i, int j)
    {
        int row = grid.size();
        int col = grid[0].size();
        grid[i][j]='0';//visited
        if(i-1>=0 && grid[i-1][j]=='1')
        {
            dfs(grid,i-1,j);
        }
        if(i+1<row && grid[i+1][j]=='1')
        {
            dfs(grid,i+1,j);
        }
        if(j-1>=0 && grid[i][j-1]=='1')
        {
            dfs(grid,i,j-1);
        }
        if(j+1<col && grid[i][j+1]=='1')
        {
            dfs(grid,i,j+1);
        }
    }
    int numIslands(vector<vector<char>>& grid) {
        int res = 0;
        for(int i = 0; i < grid.size();i++)
        {
            for(int j = 0; j < grid[0].size();j++)
            {
                if(grid[i][j]=='1')
                {
                    res++;
                    dfs(grid,i,j);
                }
            }
        }
        return res;
    }
};
