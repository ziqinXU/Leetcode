class Solution {
public:
    bool checkIfPangram(string sentence) {
        vector<int>alphabet(26,0);
        for(int i = 0; i < sentence.length(); i++)
        {
            alphabet[sentence[i]-'a']++;
        }
        for(int i = 0; i < 26; i++)
        {
            if(alphabet[i] == 0)
            {
                return false;
            }
        }
        return true;
    }
};
