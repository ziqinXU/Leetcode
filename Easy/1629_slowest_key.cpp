class Solution {
public:
    char slowestKey(vector<int>& releaseTimes, string keysPressed) {
        map<char,int> keymap;
        keymap[keysPressed[0]]=releaseTimes[0]-0;
        for(int i=1;i<keysPressed.size();i++)
        {
            if ( keymap.find(keysPressed[i]) == keymap.end() )
                keymap[keysPressed[i]]=releaseTimes[i]-releaseTimes[i-1];
            else
            {
                if(releaseTimes[i]-releaseTimes[i-1]>keymap[keysPressed[i]] )
                {
                    keymap[keysPressed[i]]=releaseTimes[i]-releaseTimes[i-1];
                }
            }
        }
        int max_value=0;
        char res='a';
       for(auto map:keymap)
        {
            if(map.second>max_value )
            {
               
                max_value=map.second;
                res=map.first;
            }
            else if(map.second == max_value && map.first > res )
            {
                 max_value=map.second;
                res=map.first;
            }
        }

    return res;
    }
};
