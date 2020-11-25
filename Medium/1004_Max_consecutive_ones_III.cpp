class Solution {
public:
    int longestOnes(vector<int>& A, int K) {
        //滑动窗口最多0个数,right为0，则count+1，left为0，count-1，缩小窗口
        int res=0;
        int zeros=0;
        int left=0,right=0;
        int count=0;
        while(right<A.size())
        {
            
            if(A[right]==0)
            {
                count++;
                
            }
            while(count>K)
            {
                if(A[left]==0)
                {
                    left++;
                    count--;
                }
                else
                {
                    left++;
                }
            }
            if(right-left+1>res)
            {
                res=right-left+1;
            }
            right++;
        }
        return res;
    }
};
