class Solution {
public:
    int calculateTime(string keyboard, string word) {
        map<char, int> hashmap;//使用hashmap统计位置
        for(int i = 0; i < keyboard.size();i ++)
        {
            hashmap[keyboard[i]]=i;
        }
        int pre = 0;
        int sum = 0;
        for(int i = 0; i < word.size();i++ )
        {
            sum += abs(hashmap[word[i]]-pre);
            pre = hashmap[word[i]];
        }
        return sum;
    }
};
