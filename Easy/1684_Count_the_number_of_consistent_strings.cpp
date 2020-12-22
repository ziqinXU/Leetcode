class Solution {
public:
    int countConsistentStrings(string allowed, vector<string>& words) {
        vector<int> hashmap(26,0);
        int count = 0;
        for(int i = 0; i< allowed.length();i++)
        {
            hashmap[allowed[i]-'a']++;
        }
        
        for(int i = 0; i < words.size();i++)
        {
            int flag = 0;
            
            for(int j = 0; j < words[i].length();j++)
            {
                
                if(hashmap[words[i][j]-'a']==0)
                {
                    flag=1;
                    break;
                }
            }
            if(flag == 0)
            count++;
        }
        return count;
    }
};
