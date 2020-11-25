class Solution {
public:
    string originalDigits(string s) {
        int nums[10] = {0};
        string res = "";
        nums[0] = count(s.begin(),s.end(),'z');
        nums[2] = count(s.begin(),s.end(),'w');
        nums[4] = count(s.begin(),s.end(),'u');
        nums[6] = count(s.begin(),s.end(),'x');
        nums[8] = count(s.begin(),s.end(),'g');
        nums[3] = count(s.begin(),s.end(),'h')-nums[8];
        nums[5] = count(s.begin(),s.end(),'f')-nums[4];
        nums[7] = count(s.begin(),s.end(),'s')-nums[6];
        nums[9] = count(s.begin(),s.end(),'i')-nums[8]-nums[5]-nums[6];
        nums[1] = count(s.begin(),s.end(),'n')-nums[7]-nums[9]*2;
        
        for(int i=0;i < 10; i++)
        {
            while(nums[i]>0)
            {
                res += ('0'+i);
                nums[i]--;
            }
        }
        return res;
    }
};
