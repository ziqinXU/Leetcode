class Solution {
public:
    string reformatNumber(string number) {
        string newnumberstring = "";
        string res = "";
        for(int i = 0; i < number.length();i++)
        {
            if(isdigit(number[i]))
            {
                newnumberstring+=number[i];
            }
        }
        
        if(newnumberstring.length()%3 == 0)
        {
            for(int i = 0; i < newnumberstring.length();i++)
            {
                if(i % 3 ==2 && i != newnumberstring.length()-1)
                {
                    res += newnumberstring[i];
                    res += "-";
                }
                else
                {
                    res += newnumberstring[i];
                }
            }
        }
        if(newnumberstring.length()%3 == 1)
        {
            for(int i = 0; i < newnumberstring.length()-4;i++)
            {
                if(i % 3 ==2)
                {
                    res += newnumberstring[i];
                    res += "-";
                }
                else
                {
                    res += newnumberstring[i];
                }
            }
            res += newnumberstring[newnumberstring.length()-4];
            res += newnumberstring[newnumberstring.length()-3];
            res += "-";
            res += newnumberstring[newnumberstring.length()-2];
            res += newnumberstring[newnumberstring.length()-1];

        }
        if(newnumberstring.length()%3 == 2)
        {
            for(int i = 0; i < newnumberstring.length()-2;i++)
            {
                if(i % 3 ==2)
                {
                    res += newnumberstring[i];
                    res += "-";
                }
                else
                {
                    res += newnumberstring[i];
                }
            }
            res += newnumberstring[newnumberstring.length()-2];
            res += newnumberstring[newnumberstring.length()-1];

        }
        return res;
    }
};
