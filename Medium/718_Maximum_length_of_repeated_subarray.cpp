///first attempt 59.12%faster, 100%less memory
//Idea:Check the positions where elements in A and in B are the same. Use Dynamic programming to check the diagnal elements
class Solution {
public:
    int findLength(vector<int>& A, vector<int>& B) {//if elements in A and in B are the same, remember the position
    int matrix[1000][1000]={0};
    int maxlength=0;
    for(int i=0;i<B.size();i++)
    {
        for(int j=0;j<A.size();j++)
        {
            if(B[i]==A[j])
            matrix[i][j]=1;
         
        }
     
    }
    for(int i=1;i<B.size();i++)//check the diagnal elements in i-1,j-1 position, if current and last elements are not 0, add 1 
    {
        for(int j=1;j<A.size();j++)
        {
            if(matrix[i-1][j-1]!=0&&matrix[i][j]!=0)
            matrix[i][j]=matrix[i-1][j-1]+1;
            if(matrix[i][j]>maxlength)
            maxlength=matrix[i][j];
        }
    }
    return maxlength;
    }
};
