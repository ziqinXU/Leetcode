class Solution {
public:
    void dfs(vector<int> & visited,vector<vector<int>>& isConnected,int i )
    {
        for(int j = 0; j < isConnected.size();j++)
        {
            
            if(visited[j] == 0 && isConnected[i][j] == 1)
            {
                visited[j] = 1;
                dfs(visited,isConnected,j);
            }
        }
        
    }

    int findCircleNum(vector<vector<int>>& isConnected) {
        vector<int> visited (isConnected.size(),0);
        int count = 0;
        for(int i = 0; i < isConnected.size();i++)
        {
            if (visited[i] == 0)
            {
                visited[i] = 1;
                dfs(visited,isConnected,i);
                count++;
            }
        }
        return count;
    }
       
};
