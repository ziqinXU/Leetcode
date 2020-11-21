class Solution {
public:
    int countBattleships(vector<vector<char>>& board) {
        //每次检查当前为X时，左边和上面是否为X
        if(board[0].size()==0)
            return 0;
        int count=0;
        if(board[0][0]=='X')
            count++;
        for(int i=1;i<board.size();i++)
        {
            if(board[i][0]=='X' && board[i-1][0]!='X')
            {
                count++;
            }
        }
        for(int j=1;j<board[0].size();j++)
        {
            if(board[0][j]=='X' && board[0][j-1]!='X')
            {       
                count++;
            }
        }
        for(int i=1;i<board.size();i++)
        {
            for(int j=1;j<board[0].size();j++)
            {
                if (board[i][j]=='X')
                {
                    if(board[i][j-1]!='X' && board[i-1][j]!='X')
                    {
                       
                        count++;
                    }
                }
            }
        }
        return count;
    }
};
