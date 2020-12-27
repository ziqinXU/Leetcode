class Solution {
public:
    int minPartitions(string n) {
        //返回字符串中最大的数字
        sort(n.begin(),n.end());
        return n.back()-'0';
    }
};
