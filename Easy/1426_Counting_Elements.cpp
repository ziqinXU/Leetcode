class Solution {
public:
    int countElements(vector<int>& arr) {
        map<int,int>hashmap;
        for(int i=0;i<arr.size();i++)
        {
            hashmap[arr[i]]++;
        }
        map<int,int>::iterator it;
        int count=0;
        for(it=hashmap.begin(); it!=hashmap.end(); ++it)
        {
             if(it->first+1==(++it)->first)
            {
               count=count+(--it)->second;
            }
            else
            {
                it--;
            }
        }
        return count;
    }
};
