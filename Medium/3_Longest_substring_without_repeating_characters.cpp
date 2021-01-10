class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int i = 0, j = 0;
        std::unordered_set<char> sset;
        int returnlen = 0;
        int templen = 0;
       
        while(j<s.size())
        {
            if(sset.find(s[j]) == sset.end()) //NOT FOUND IN SET
            {
                sset.insert(s[j]);
            }
            else
            {
                int index = s.substr(i,j-i).find(s[j])+i;
                
                templen = j-i;
                if(templen > returnlen)
                {
                    returnlen = templen;
                }
                i = index+1;
                
            }
            j++;
            
        }
        templen = j-i;
        if(templen > returnlen)
        {
            returnlen = templen;
        }
        return returnlen;
    }
};
