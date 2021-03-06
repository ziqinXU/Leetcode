class Solution {
public:
    bool validWordSquare(vector<string>& words) {
        string temp;
        int diff;
        for(int i=0;i<words.size();i++)
        {
            diff=words.size()-words[i].size();
            if(diff<0)
            return false;
            if(diff>0)
            {
                while(diff!=0)
                {
                    words[i].push_back(' ');
                    diff--;
                }
                
            }
        }
        
        for(int j=0;j<words.size();j++)
        {
            for(int i=0;i<words.size();i++)
            {
                temp.push_back(words[i][j]);
            }
            if(words[j]!=temp)
            return false;
            temp.clear();
            
        }
        return true;
    }
};

