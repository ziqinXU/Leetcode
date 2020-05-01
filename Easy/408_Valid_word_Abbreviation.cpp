///first attempt 64.08%faster, 100%less memory
//Idea:go through string word and check corresponding positions with rules in string abbr. 
//Convert abbr into alphabet and numbers.
class Solution {
public:
    bool validWordAbbreviation(string word, string abbr) {
        int pos=0;
        int number;
        string numberstring;
        int i;
        for(i=0;i<abbr.size();i++)
        {
            if(abbr[i]<='z'&&abbr[i]>='a')//if in abbr there is an alphabet, check the corresponding positions in word
            {
                if(word[pos]!=abbr[i])
                return false;
                pos++;
                 //printf("%d",i);
            }
            if(abbr[i]<='9'&&abbr[i]>='0')//if there is a number, iterate until next alphabet appears.
            {
                if(abbr[i]=='0')
                return false;
                numberstring.push_back(abbr[i]);
                
                int j=i+1;
                while(j<abbr.size()&&(abbr[j]<='9'&&abbr[j]>='0'))
                {
                    numberstring.push_back(abbr[j]);
                    j++;
                }
                i=j-1;
                pos=pos+(stoi(numberstring));
                numberstring.clear();
                if(pos>word.size())
                return false;
            }
        }
       
        if(word.size()!=pos)//check whether the checking process reaches the end of string word 
        return false;
        return true;
    }
};
