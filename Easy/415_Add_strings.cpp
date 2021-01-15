class Solution {
public:
    string addStrings(string num1, string num2) {
        //到序相加，进位数字保存
        string res = "";
        int i = num1.length()-1 ,j = num2.length()-1 , tempsum = 0, add = 0;
        while(i >= 0 || j >= 0 || add !=0)
        {
            
            tempsum = (i>= 0 ? (num1[i]-'0') % 10:0) + (j>= 0 ?(num2[j]-'0') % 10 :0) + add;
            if(tempsum / 10 == 1)
            {
                add = 1;
            }
            else
            {
                 add = 0;
            }
            res += tempsum % 10 +'0';
            
            i--;
            j--;
        }
        reverse(res.begin(),res.end());
        return res;
    }
};
