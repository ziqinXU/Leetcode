class Solution {
public:
    int longestMountain(vector<int>& arr) {
        int maxlen = 0;
        for(int i = 1; i< arr.size()-1;i++)
        {
            if(arr[i-1] < arr[i] && arr[i] > arr[i+1])
            {
                int left = i-2;
                while(left>= 0 && arr[left]< arr[left+1])
                {
                    left--;
                }
                int right = i+2;
                while(right < arr.size() && arr[right]< arr[right-1])
                {
                    right++;
                }
                
                if(right-left-1> maxlen)
                {
                    maxlen = right-left-1;
                }
            }
        }
        return maxlen;
    }
};
