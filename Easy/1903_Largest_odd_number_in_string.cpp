class Solution {
public:
    string largestOddNumber(string num) {
        string res = "";
        for(int i = num.length() - 1; i >= 0; i--)
        {
            if(int(num[i]) % 2 == 1)
            {
                res = num.substr(0, i + 1);
                return res;
            }
        }
        return res;
    }
};
