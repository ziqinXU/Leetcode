class Solution {
public:
    bool isToeplitzMatrix(vector<vector<int>>& matrix) {
        if(matrix.size()==0)
        return true;
        if(matrix.size()==1)
        return true;
        vector<int>temp;
        int m,k;
        for(int i=0;i<matrix.size();i++)
        {
            m=i;
            k=0;
            while(m<matrix.size()&&k<matrix[0].size())
            {
                temp.push_back(matrix[m][k]);
                m++;
                k++;
            }
            sort(temp.begin(),temp.end());
            if(temp[0]!=temp[temp.size()-1])
            return false;
            temp.clear();
        }
        for(int j=1;j<matrix[0].size();j++)
        {
            m=0;
            k=j;
            
            while(m<matrix.size()&&k<matrix[0].size())
            {
                temp.push_back(matrix[m][k]);
                m++;
                k++;
            }
           
            sort(temp.begin(),temp.end());
           
            if(temp[0]!=temp[temp.size()-1])
            return false;
            temp.clear();
        }
        return true;
    }
};
