class Solution {
public:
    int maximumUnits(vector<vector<int>>& boxTypes, int truckSize) {
        sort(boxTypes.begin(),boxTypes.end(),[](const auto& L, const auto& R){return L[1] > R[1];}); //从大到小排序
        int returnvalue = 0;
        for(int i = 0; i < boxTypes.size();i++)
        {
            if(truckSize-boxTypes[i][0]>=0)
            {
                returnvalue += boxTypes[i][1]*boxTypes[i][0];
                truckSize -= boxTypes[i][0];
            }
            else
            {
                if(truckSize > 0)
                {
                    returnvalue += boxTypes[i][1]*truckSize;
                    truckSize = 0;
                }
                else
                {
                    break;
                }
            }
        }
        return returnvalue;
    }
};
