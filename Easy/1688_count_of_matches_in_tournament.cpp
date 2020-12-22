class Solution {
public:
    int numberOfMatches(int n) {
        int left = n;
        int match = 0;
        int res = 0;
        while(left!=1)
        {
            if(left % 2 == 0)
            {
                match = left/2;
                left = left/2;
            }
            else
            {
                match = (left-1)/2;
                left = (left-1)/2+1;
            }
            res += match;
        }
        return res;
    }
};
