///first attempt 23.55%faster, 100%less memory
//Idea: use hashmap to count alphabets and their frequency, sort the array according to their frequency
//insert the odd position first from the most frequent alphabet and then insert alpabet in the even position
//if the most frequent alphabet is greater than half of the string, return ""
class Solution {
public:
    string reorganizeString(string S) {
    map<char,int>hashmap;
    string returnarray;
    pair<int,char>temp[500];
    vector<pair<int,char>>countalphabet;
    for(int i=0;i<S.size();i++)
    {
        hashmap[S[i]]++;
    }
    for(int i=0;i<26;i++)
    {
        if(hashmap[i+'a']>(S.size()/2+S.size()%2))// the frequency is more than the half, no required string
        return "";
        if(hashmap[i+'a']!=0)
        {
            temp[i].first=hashmap[i+'a'];
            temp[i].second=i+'a';
            countalphabet.push_back(temp[i]);
        }

    }
    sort(countalphabet.begin(),countalphabet.end(),greater<>());//sort array with descending order and according to their frequency
    string newarray;
  
    for(int i=0;i<countalphabet.size();i++)//convert it again into a newstring
    {
        while(countalphabet[i].first!=0)
        {
            newarray.push_back(countalphabet[i].second);
            countalphabet[i].first--;
        }
        
    }

    int p=0;
    int m=S.size()/2+S.size()%2;
    for(int i=0;i<S.size();i++)//insert odd positions first,then the even positions.
    {
        if(i%2==0)
        {
        returnarray.push_back(newarray[p]);
        p++;
        }
        else
        {
        returnarray.push_back(newarray[m]);
        m++;
        }
        //printf("%d ",i);
        
    }
    
    
    
    return returnarray;
    }
};
