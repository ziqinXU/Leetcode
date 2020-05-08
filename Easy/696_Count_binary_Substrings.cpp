///first attempt 5.78%faster, 100%less memory
//Idea:find '10' and '01' then expand them forward and backward with 1 and 0 respectively
class Solution {
public:
    int countBinarySubstrings(string s) {
    int k=-1;
    int k1=0;
    int count=0;
    while(k1!=-1)
    {
        k1=s.find("10",k+1);//find all "10"
        k=k1;
        if(k1==-1)
        break;
        count++;
        int i=1,j=2;
       
        while(k1-i>=0&&k1+j<s.size())//check wether backwards are 1s and forward are 0s
        {
           
            if(s[k1-i]=='1'&&s[k1+j]=='0')
            {
                
                 count++;
                 i++;
                 j++;
            }
           
            else
            break;
        }
    }
    
    k=-1;
    k1=0;
   while(k1!=-1)
    {
        k1=s.find("01",k+1);//find all "01" and rest similar as above
        k=k1;
        if(k1==-1)
        break;
        count++;
        int i=1,j=2;
        while(k1-i>=0&&k1+j<s.size())
        {
            if(s[k1-i]=='0'&&s[k1+j]=='1')
            {
                 count++;
                 i++;
                 j++;
            }
           
            else
            break;
        }
    }
    
    return count;
    }
};
