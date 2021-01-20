class Solution {
public:
    static bool checkdescent(const pair<char,int> &a, const pair<char,int> &b)
    {
        return a.second>b.second;
    }
string frequencySort(string s) {
        string res="";
        vector<pair<char,int>>v;
        map<char,int> count;
        for(int i = 0; i<s.length();i++)
        {
            if(count.find(s[i])!=count.end())
            {
                count[s[i]]++;
            }
            else
            {
                count[s[i]] = 1;
            }
        }
        for(map<char,int>::iterator it = count.begin();it!=count.end();it++)
        {
            v.push_back(make_pair(it->first,it->second));
        }
        sort(v.begin(),v.end(),checkdescent);
        for(int i = 0; i< v.size();i++)
        {

            while(v[i].second>0)
            {
                res += v[i].first;
                v[i].second--;
            }

        }
        return res;
    }
};
