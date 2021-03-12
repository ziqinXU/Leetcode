class Solution {
public:
    string mergeAlternately(string word1, string word2) {
        string returnstring = "";
        if(word1.size()>=word2.size())
        {
            for(int i = 0; i < word2.size();i++)
            {
                returnstring += word1[i];
                returnstring += word2[i];
            }
            returnstring += word1.substr(word2.size(),word1.size()-word2.size());
        }
        else
        {
            for(int i = 0; i < word1.size();i++)
            {
                returnstring += word1[i];
                returnstring += word2[i];
            }
            returnstring += word2.substr(word1.size(),word2.size()-word1.size());
        }
        return returnstring;
    }
};
