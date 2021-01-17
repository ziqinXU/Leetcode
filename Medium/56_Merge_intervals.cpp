class Solution {
public:
    vector<vector<int>> merge(vector<vector<int>>& intervals) {
        vector<vector<int>> res;
        sort(intervals.begin(),intervals.end());
        int fl = intervals[0][0];
        int fr = intervals[0][1];
        res.push_back({intervals[0][0],intervals[0][1]});
        for(int i = 1; i < intervals.size();i++)
        {
            int sl = intervals[i][0];
            int sr = intervals[i][1];
            
            if (sl-fr > 0)
            {
                res.push_back({intervals[i][0],intervals[i][1]});
            }
            else
            {
                int resback = res.back()[1];
                int resfront = res.back()[0];
                res.pop_back();
                res.push_back({
                    resfront,max(intervals[i][1],resback)});   
            }
            fl = res.back()[0];
            fr = res.back()[1];
            
        }
        return res;
    }
};
