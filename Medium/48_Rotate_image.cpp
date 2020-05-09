class Solution {
public:
    void rotate(vector<vector<int>>& matrix) {
        int temp;
        for(int i=0;i<matrix.size();i++)
        {
            for(int j=0;j<i+1;j++)
            {
                if(i!=j)
                {
                    temp=matrix[i][j];
                    matrix[i][j]=matrix[j][i];
                    matrix[j][i]=temp;
                }
            }
        }
        for(int i=0;i<matrix.size();i++)
        {
            for(int j=0;j<matrix[i].size()/2;j++)
            {
                temp=matrix[i][j];
                matrix[i][j]=matrix[i][matrix[i].size()-1-j];
                matrix[i][matrix[i].size()-1-j]=temp;
            }
        }
        
        

    }
};
