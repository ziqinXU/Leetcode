///first attempt 10.83%faster, 5.26%less memory
//Idea:Check the four cells around the current cell, if the current one is 1 and the side number of current cell
//is 4-number of cells around current one.
class Solution {
public:
    int surrounding(int r,int c, int i, int j,vector<vector<int>>& grid)//check the side number
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
            if(grid[i][j]==1)//if the current cell is equal to one, check its surroundings.
            {
                count=count+surrounding(grid.size(),grid[i].size(),i,j,grid);
            }
        }
 
    }
   
    return count;
    }
};
