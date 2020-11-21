class Solution {
public:
        static bool cmp( vector<int> a,  vector<int> b) 
        {
             if(a[0]==b[0])
            return a[1]<b[1];
            return a[0]>b[0];
        }
    vector<vector<int>> reconstructQueue(vector<vector<int>>& people) {
        vector<vector<int>> res;
        if(people.size()==0)
        return res;
        sort(people.begin(),people.end(),cmp);
        int len=0;
        
        for(int i=0;i<people.size();i++)
        {
           if(people[i][1]<=len)
           {
               res.insert(res.begin()+people[i][1],people[i]);
           }
           else
           {
               res.push_back(people[i]);
           }
           len++;
        }
        return res;
    
    }
};
