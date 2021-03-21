class Solution {
public:
    bool areAlmostEqual(string s1, string s2) {
        string s1_cut = "";
        string s2_cut = "";
        int count = 0;
        
        for(int i = 0; i < s1.length();i++)
        {
            if(s1[i]!=s2[i])
            {
                s1_cut += s1[i];
                s2_cut += s2[i];
                count ++;
            }
            if(count>2)
            return false;
        }
        if(count == 0)
        return true;
        if(s1_cut[0] == s2_cut[1] && s1_cut[1] == s2_cut[0])
        return true;
        else
        return false;

    }
};
