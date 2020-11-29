class Solution {
public:

    int maxKilledEnemies(vector<vector<char>>& grid) {
        int res=0;
        for(int i=0;i<grid.size();i++)
        {
            for(int j=0;j<grid[0].size();j++)
            {
                if(grid[i][j]=='0')
                {
                    int count=0;
                    int newi=i,newj=j;
                    while(--newi>=0)
                    {
                        
                        if(grid[newi][j]=='W')
                        {   
                            break;
                        }
                        if(grid[newi][j]=='E')
                        {
                            count++;
                        }
                        
                    }
                    
                    while(--newj>=0)
                    {
                        if(grid[i][newj]=='W')
                        {   
                            break;
                        }
                        if(grid[i][newj]=='E')
                        {
                            count++;
                        }
                        
                    }
                    
                    newi=i,newj=j;
                    while(++newi<grid.size())
                    {
                        if(grid[newi][j]=='W')
                        {   
                            break;
                        }
                        if(grid[newi][j]=='E')
                        {
                            count++;
                        }
                        
                    }
                    
                    while(++newj<grid[0].size())
                    {
                        if(grid[i][newj]=='W')
                        {   
                            break;
                        }
                        if(grid[i][newj]=='E')
                        {
                            count++;
                        }
                        
                    }  
                    if(count>=res)
                    {
                        res=count;
                    }
                }
            }
        }
        return res;
    }
    

};
