class Solution {
public:
    bool halvesAreAlike(string s) {
        set<int> sset;
        sset.insert('a');
        sset.insert('e');
        sset.insert('i');
        sset.insert('o');
        sset.insert('u');
        sset.insert('A');
        sset.insert('E');
        sset.insert('I');
        sset.insert('O');
        sset.insert('U');
        string first = s.substr(0,s.length()/2);
        string second = s.substr(s.length()/2,s.length()/2);
        int totalfirst = 0;
        int totalsecond = 0;
        for(auto i:first)
        {
            if(sset.find(i)!=sset.end())
            {
                totalfirst += 1;
            }
        }
        for(auto i:second)
        {
            if(sset.find(i)!=sset.end())
            {
                totalsecond += 1;
            }
        }
        if(totalfirst == totalsecond)
        return true;
        else
        return false;
    }
};
