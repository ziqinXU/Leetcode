class Solution {
public:
    bool validWordAbbreviation(string word, string abbr) {
        int pos=0;
        int number;
        string numberstring;
        int i;
        for(i=0;i<abbr.size();i++)
        {
            if(abbr[i]<='z'&&abbr[i]>='a')
            {
                if(word[pos]!=abbr[i])
                return false;
                pos++;
                 //printf("%d",i);
            }
            if(abbr[i]<='9'&&abbr[i]>='0')
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
              // printf("%d",pos);
                numberstring.clear();
                if(pos>word.size())
                return false;
            }
        }
       // printf("%d %d",i,pos);
        if(word.size()!=pos)
        return false;
        return true;
    }
};
