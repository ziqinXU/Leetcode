class Solution {
public:
    string longestPalindrome(string s) {
    //DP
        vector<vector<bool> >dp(s.length(),vector<bool>(s.length(),true));
        int maxlen = 1;
        int pos = 0;
        for(int j = 1; j < s.length();j++)
        {
            for(int i = 0; i < j;i++)
            {
                if(s[i]!=s[j])
                {
                    dp[i][j]=false;
                }
                else
                {
                        if(dp[i+1][j-1]==true)
                        {
                            
                            dp[i][j]=true;
                            if(j-i+1>maxlen)
                        {
                            maxlen = j-i+1;
                            pos = i;
                        }
                        
                    }
                    else
                    {
                        dp[i][j]=false;
                    }
                    
                }
                
            }
        }

        return s.substr(pos,maxlen);
    }
};
