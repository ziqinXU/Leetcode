///first attempt 30.75%faster, 25%less memory
//Idea:Add the sum of original array A first and then check the odevity of the number in A and in queries and classify them into four cases.
class Solution {
public:
    vector<int> sumEvenAfterQueries(vector<int>& A, vector<vector<int>>& queries) {
    int sum=0;
    vector<int>returnarray;
    for(int i=0;i<A.size();i++)//add all elements in A together
    {
        if(A[i]%2==0)
        sum=sum+A[i];
    }
   
    for(int i=0;i<queries.size();i++)
    {
       
        if(abs(queries[i][0])%2==0&&abs(A[queries[i][1]])%2==0)//if both of them are even,add the number in queries
        {
            sum=sum+queries[i][0];
            returnarray.push_back(sum);
            
        }
        else if(abs(queries[i][0])%2==1&&abs(A[queries[i][1]])%2==1)//if both of them are odd,add both
        {
            sum=sum+queries[i][0]+A[queries[i][1]];
            
            returnarray.push_back(sum);
            
        }
        else if(abs(queries[i][0])%2==0&&abs(A[queries[i][1]]%2)==1)//even+odd=even,keep the same
        {
            sum=sum;
            returnarray.push_back(sum);
            
        }
        else if(abs(queries[i][0])%2==1&&abs(A[queries[i][1]]%2)==0)//even+odd=even,the number in A should be removed
        {
            sum=sum-A[queries[i][1]];
            returnarray.push_back(sum);
           
        }
         A[queries[i][1]]=A[queries[i][1]]+queries[i][0];//do changes
         
    }
    return returnarray;
    }
};
