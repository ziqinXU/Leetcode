class Solution {
public:
    int countVowelStrings(int n) {
        //n+5小球到5个盒子里，可空盒子
        return (n + 4) * (n + 3) * (n + 2) * (n + 1) / 24;
    }
};
