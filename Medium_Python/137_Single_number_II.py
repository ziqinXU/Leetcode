//#每位均出现3次，除了一个数字,用python会涉及到负数问题
class Solution {
public:
    int singleNumber(vector<int>& nums) {
        int digits[32] = {0};
        for(int i=0; i<32; i++)
        {
            for(int j=0; j<nums.size(); j++)
            {
                digits[i] = digits[i] + ((nums[j]>>i)&1); //每位上数字和 += 比较好，= A+B需要注意这里有涉及位运算的优先级问题
            }
        }
        int res=0;
        for(int i=31; i>=0; i--)
        {
            res += (digits[i]%3)<<i;
        }
        return res;
    }
};
