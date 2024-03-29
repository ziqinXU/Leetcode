class Solution {
public:
    int secondHighest(string s) {
        int arr[10] = {0};
        int count = 0;
        for(int i = 0; i < s.length();i++)
        {
            if(s[i] - '0' >= 0 && s[i] - '0' <= 9)
            {
                arr[s[i] - '0']++;
            }
        }
        for(int i = 9; i >= 0; i--)
        {
            if(arr[i] != 0)
            {
                count++;
            }
            if(count == 2)
            return i;
        }
        return -1;
    }
};
