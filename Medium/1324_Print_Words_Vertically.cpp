class Solution {
public:
    vector<string> printVertically(string s) {
    vector<string>spiltstring;
    vector<string>returnarray;
    int first=0;
    int count[1000];
    int p=0;
    string tempstring;
    for(int i=0;i<s.size();i++)
    {
        if(s[i]==' ')
        {
            tempstring=s.substr(first,i-first);
            spiltstring.push_back(tempstring);
            tempstring.clear();
            count[p]=i-first;
            p++;
            first=i+1;
            
        }
        
    }
    spiltstring.push_back(s.substr(first,s.size()));
    count[p]=s.size()-first;
    p++;
    int maxlen=*max_element (count, count+p); //maxlen return strings
    int len=0;
   
    while(len<maxlen)
    {
        
        for(int i=0;i<p;i++)//p words
        {
            if(spiltstring[i].size()-1>=len)
            {
               
                tempstring.push_back(spiltstring[i][len]);
            }
            else
            {
                tempstring.push_back(' ');
            }
        }
        returnarray.push_back(tempstring);
        tempstring.clear();
        len++;
    }
    for(int i=0;i<returnarray.size();i++)
    {
        int k=returnarray[i].size()-1;
        while(returnarray[i][k]==' ')
        {
            returnarray[i].pop_back();
            k--;
        }
        
    }
    return returnarray;
    }
};
