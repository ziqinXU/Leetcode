class Solution {
public:
    bool checkOnesSegment(string s) {
        int count = 0;
        for(int i = 0; i < s.size();i++)
        {
            
            if(s[i] == '1')
            {
                count++;
                while(i + 1 < s.size() & s[i] == s[i+1])
                {
                    i++;
                }
                
            }   
        }
        if(count > 1)
        {
            return false;
        }
        return true;
        
    }
};
