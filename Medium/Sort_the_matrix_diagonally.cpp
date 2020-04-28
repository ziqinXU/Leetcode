class Solution {
public:
    vector<vector<int>> diagonalSort(vector<vector<int>>& mat) {
        if(mat.size()==0)
        return mat;
        vector<int>temp;
        int m,k;
        for(int i=0;i<mat.size();i++)
        {
            m=i;
            k=0;
            while(m<mat.size()&&k<mat[0].size())
            {
                temp.push_back(mat[m][k]);
                m++;
                k++;
            }
            sort(temp.begin(),temp.end());

            m=i;
            k=0;
            int p=0;
            while(m<mat.size()&&k<mat[0].size())
            {
                mat[m][k]=temp[p];
                p++;
                m++;
                k++;
            }

            temp.clear();
        }
        for(int j=1;j<mat[0].size();j++)
        {
            m=0;
            k=j;
            
            while(m<mat.size()&&k<mat[0].size())
            {
                temp.push_back(mat[m][k]);
                m++;
                k++;
            }
           
            sort(temp.begin(),temp.end());
            m=0;
            k=j;
            int p=0;
            while(m<mat.size()&&k<mat[0].size())
            {
                mat[m][k]=temp[p];
                p++;
                m++;
                k++;
            }

            temp.clear();
           
        }
       return mat;
    }
};
