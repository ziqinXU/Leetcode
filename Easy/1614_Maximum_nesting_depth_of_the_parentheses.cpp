class Solution {
public:
    int maxDepth(string s) {
        vector<char> arr;//vector 能达到的最大长度
        int count=0;
        int maxcount=0;
        for(int i=0; i < s.size(); i++)
        {
            if(s[i]=='(')
            {
                arr.push_back('(');
                count++;
            }
            if(s[i]==')')
            {
                arr.pop_back();
                count--;
            }
            
            if(count>maxcount)
            {
                maxcount=count;
            }
        }
        
        return maxcount;
    }
};
