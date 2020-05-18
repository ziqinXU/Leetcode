class Solution {
public:
    vector<int> sumEvenAfterQueries(vector<int>& A, vector<vector<int>>& queries) {
    int sum=0;
    vector<int>returnarray;
    for(int i=0;i<A.size();i++)
    {
        if(A[i]%2==0)
        sum=sum+A[i];
    }
   
    for(int i=0;i<queries.size();i++)
    {
       
        if(abs(queries[i][0])%2==0&&abs(A[queries[i][1]])%2==0)
        {
            sum=sum+queries[i][0];
            returnarray.push_back(sum);
            
        }
        else if(abs(queries[i][0])%2==1&&abs(A[queries[i][1]])%2==1)
        {
            sum=sum+queries[i][0]+A[queries[i][1]];
            
            returnarray.push_back(sum);
            
        }
        else if(abs(queries[i][0])%2==0&&abs(A[queries[i][1]]%2)==1)
        {
            sum=sum;
            returnarray.push_back(sum);
            
        }
        else if(abs(queries[i][0])%2==1&&abs(A[queries[i][1]]%2)==0)
        {
            sum=sum-A[queries[i][1]];
            returnarray.push_back(sum);
           
        }
         A[queries[i][1]]=A[queries[i][1]]+queries[i][0];
         
    }
    return returnarray;
    }
};
