class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        //二分法找出分别的分割线右边的index，再对附近的4个数字进行处理。
        int nums1len = nums1.size();
        int nums2len = nums2.size();
        
        vector<int>temp;
        if (nums1len>nums2len)
        {
            temp = nums1;
            nums1 = nums2;
            nums2 = temp;
        }
        nums1len = nums1.size();
        nums2len = nums2.size();
        int left = 0;
        int right = nums1len;
        int i,j;
        
        while(left < right)
        {
            i = left + (right-left+1)/2;
            j = (nums1len+nums2len+1)/2-i;
            
            if(nums1[i - 1] > nums2[j])
            {
                right = i - 1;
            }
            else
            {
                left = i;
            }
            
        }
        
        i = left;
        j = (nums1len+nums2len+1)/2-i;
        if(nums1len == 0)
        {
            if(nums2len % 2 ==0)
            {
                return (nums2[j]+nums2[j-1])/2.0;
            }
            else
            {
                return nums2[j-1];
            }
        }
        int nums1left = (i == 0 ? INT_MIN : nums1[i-1]);
        int nums1right = (i == nums1len ? INT_MAX:nums1[i]);
        int nums2left = (j == 0 ? INT_MIN:nums2[j-1]);
        int nums2right = (j == nums2len ? INT_MAX:nums2[j]);

        if( (nums1len + nums2len ) % 2 == 1)
        {
            return max(nums1left,nums2left);
        }
        else
        {
            return (max(nums1left,nums2left)+min(nums1right,nums2right))/2.0;
        }
        return 0;
    }
};
