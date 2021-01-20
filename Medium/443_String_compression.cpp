class Solution {
public:
    int compress(vector<char>& chars) {
        int left = 0;
        int right = 0;
        int cur = 0;
        int len = 0;
        while(right < chars.size())
        {
            while(right < chars.size() && chars[right] == chars[left])
            {
                right++;
            }
            
            len = right-left;
            
            if(len>1)
            {
                int start = cur+1;
                chars[cur] = chars[left];
                while(len/10!=0)
                {
                    chars[cur+1] = len%10 + '0';
                    cur++;
                    len /= 10;
                }
                
                chars[cur+1] = len%10 + '0';
                int end = cur+1;
                for(int j = 0; j <(end-start+1)/2;j++ )
                {
                    
                    char temp ;
                    temp = chars[j+start];
                   
                    chars[j+start] = chars[end-start+1-j-1+start];
                    chars[end-start+1-j-1+start] = temp;
                }
                cur+=2;
                
            }
            else
            {
                chars[cur] = chars[left];
                cur++;
            }
            
            left = right;
           
        }
        return cur;
    }
};
