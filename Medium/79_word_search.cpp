class Solution {
public:
    bool dfs(vector<vector<char>>& board, vector<vector<bool>>& visited,int i, int j, int pos, string word)
    {
        if(board[i][j]!=word[pos]){ // not the same
            return false;
        }

        else if(pos==word.size()-1){ //read end
        
            return true;
        }
       
            visited[i][j]=true;
            pos++;
            if((i-1>=0 && visited[i-1][j] == false && dfs(board,visited,i-1,j,pos,word) )|| (i+1<board.size() && visited[i+1][j] == false &&dfs(board,visited,i+1,j,pos,word) ) || (j-1>=0 && visited[i][j-1] == false && dfs(board,visited,i,j-1,pos,word)) || (j+1< board[0].size() && visited[i][j+1] == false && dfs(board,visited,i,j+1,pos,word)))
            return true;
            visited[i][j] = false;
            return false;
       
        
    }
    bool exist(vector<vector<char>>& board, string word) {
        bool flag;
        for(int i = 0; i< board.size();i++)
        {
            for(int j = 0; j < board[0].size();j++)
            {
                if(board[i][j] == word[0])
                {
                    vector<vector<bool>> visited(board.size(),vector<bool>(board [0].size(),false));
                    visited[i][j]=true;
                    flag = dfs(board,visited,i,j,0,word);
                    
                    if(flag == true)
                    return true;
                }
            }
        }
        return false;

    }
};
