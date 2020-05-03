///first attempt 63.64%faster, 100%less memory
//Idea:use hashmap to count, iterator through hashmap, check whether the current element plus one is equal to the next element,
//if so, add the current element frequency.
class Solution {
public:
    int countElements(vector<int>& arr) {
        map<int,int>hashmap;
        for(int i=0;i<arr.size();i++)//count the elements
        {
            hashmap[arr[i]]++;
        }
        map<int,int>::iterator it;
        int count=0;
        for(it=hashmap.begin(); it!=hashmap.end(); ++it)
        {
             if(it->first+1==(++it)->first)
            {
               count=count+(--it)->second;//move pointer back to the current one
            }
            else
            {
                it--;//pay attetion to the if condition above, if the condition is not satisfied, it will also move pointer to the next
            }
        }
        return count;
    }
};
