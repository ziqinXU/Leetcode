class Solution {
public:
    vector<vector<int>> shiftGrid(vector<vector<int>>& grid, int k) {
    vector<int>intarray;
    vector<vector<int>>returnarray;
    for(int i=0;i<grid.size();i++)
    {
        for(int j=0;j<grid[i].size();j++)
        {
            intarray.push_back(grid[i][j]);
        }
    }
    int p=intarray.size()-1;
    int m=k%(grid.size()*grid[0].size());
    vector<int>lastpart;
    while(m!=0)
    {
        lastpart.push_back(intarray[p]);
        p--;
        m--;
    }
    
    int q=0;
    int r=lastpart.size()-1;
    vector<int>temp;
    for(int i=0;i<grid.size();i++)
    {
        for(int j=0;j<grid[i].size();j++)
        {
            if(r!=-1)
            {
                temp.push_back(lastpart[r]);
                
                r--;
                
            }
            else
            {
                temp.push_back(intarray[q]);
                q++;
            }
        }
        returnarray.push_back(temp);
        temp.clear();

    }
    return returnarray;
    }
};
