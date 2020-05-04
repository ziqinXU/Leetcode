class Solution {
public:
    int surrounding(int r,int c, int i, int j,vector<vector<int>>& grid)
    {
        int side=0;
        if(i-1>=0)
        {
            if(grid[i-1][j]==1)
            side++;
        }
        if(i+1<r)
        {
            if(grid[i+1][j]==1)
            side++;
        }
        if(j-1>=0)
        {
            if(grid[i][j-1]==1)
            side++;
        }
        if(j+1<c)
        {
            if(grid[i][j+1]==1)
            side++;
        }
        return 4-side;

    }
    int islandPerimeter(vector<vector<int>>& grid) {
    int count=0;
    for(int i=0;i<grid.size();i++)
    {
        for(int j=0;j<grid[i].size();j++)
        {
            if(grid[i][j]==1)
            {
                count=count+surrounding(grid.size(),grid[i].size(),i,j,grid);
            }
        }
 
    }
   
    return count;
    }
};
