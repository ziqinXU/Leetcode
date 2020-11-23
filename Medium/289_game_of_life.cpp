class Solution {
public:
    void gameOfLife(vector<vector<int>>& board) {
        //flag标记活->死和死->活细胞
        for(int i=0;i<board.size();i++)
        {
            for(int j=0;j<board[0].size();j++)
            {
                int count=0;
                for(int k=i-1;k<=i+1;k++)
                {
                    for(int m=j-1;m<=j+1;m++)
                    {
                            if(k>=0 && k<board.size() && m>=0 && m<board[0].size())
                            {
                                
                                if(board[k][m]==1||board[k][m]==-1)
                                count++;
                            }
                    }
                    
                }
                if(board[i][j]==1)
                    count--;
                
                if(board[i][j]==1)
                {
                    if(count<2 || count>3)
                    {
                        board[i][j]=-1;//live->dead
                    }
                }
                else
                {
                    if(count==3)
                    {
                        board[i][j]=2;//dead->live
                    }
                }
                
                

            }
        }
        for(int i=0;i<board.size();i++)
        {
            for(int j=0;j<board[0].size();j++)
            {
                if(board[i][j]==-1)
                {
                    board[i][j]=0;
                }
                if(board[i][j]==2)
                {
                    board[i][j]=1;
                }
            }
        }
    }
};
