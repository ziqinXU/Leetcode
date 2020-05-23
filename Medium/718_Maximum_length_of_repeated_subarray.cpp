class Solution {
public:
    int findLength(vector<int>& A, vector<int>& B) {
    int matrix[1000][1000]={0};
    int maxlength=0;
    for(int i=0;i<B.size();i++)
    {
        for(int j=0;j<A.size();j++)
        {
            if(B[i]==A[j])
            matrix[i][j]=1;
           // printf("%d ",matrix[i][j]);
        }
       // printf("\n");
    }
    for(int i=1;i<B.size();i++)
    {
        for(int j=1;j<A.size();j++)
        {
            if(matrix[i-1][j-1]!=0&&matrix[i][j]!=0)
            matrix[i][j]=matrix[i-1][j-1]+1;
           // printf("%d %d %d    ",matrix[i][j],i,j);
            if(matrix[i][j]>maxlength)
            maxlength=matrix[i][j];
        }
    }
    return maxlength;
    }
};
