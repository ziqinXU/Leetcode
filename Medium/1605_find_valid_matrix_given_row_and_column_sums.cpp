class Solution {
public:
    vector<vector<int>> restoreMatrix(vector<int>& rowSum, vector<int>& colSum) {
        //min(rowSum[i],colSum[j]),同时减去对应的值
        vector<vector<int>> res;
        for(int i=0; i < rowSum.size();i++)
        {
            vector<int> temp;
            for(int j=0;j < colSum.size();j++)
            {
                temp.push_back(0);
                
            }
            res.push_back(temp);
            temp.clear();
        }
        for(int i=0; i < rowSum.size();i++)
        {
            for(int j=0;j < colSum.size();j++)
            {
                if(min(rowSum[i],colSum[j])>0)
                {
                    res[i][j] = min(rowSum[i],colSum[j]);
                    rowSum[i]-=res[i][j];
                    colSum[j]-=res[i][j];
                }
            }
        }
        return res;


    }
};
