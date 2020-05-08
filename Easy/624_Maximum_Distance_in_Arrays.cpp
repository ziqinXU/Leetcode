class Solution {
public:
    int maxDistance(vector<vector<int>>& arrays) {
    int max=0;
    int current;
    int temparray[3]={0};
    temparray[0]=arrays[0][0];
    temparray[1]=arrays[0][arrays[0].size()-1];
    temparray[2]=INT_MIN;
    for(int i=1;i<arrays.size();i++)
    {
        if(arrays[i][arrays[i].size()-1]-temparray[0]>temparray[1]-arrays[i][0])
        current=arrays[i][arrays[i].size()-1]-temparray[0];
        else
        current=temparray[1]-arrays[i][0];
        if(arrays[i][0]<temparray[0])
        temparray[0]=arrays[i][0];
        if(arrays[i][arrays[i].size()-1]>temparray[1])
        temparray[1]=arrays[i][arrays[i].size()-1];
        if(current>temparray[2])
        temparray[2]=current;
            
    }
    return temparray[2];
    }
};
