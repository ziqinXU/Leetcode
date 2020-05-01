///first attempt 84.07%faster, 100%less memory
//Idea:reverse string and added them up, pay attention to the length and reverse it again and conver again into string
class Solution {
public:
    string addBinary(string a, string b) {
    char temp;
    string returnarray;
    for(int i=0;i<a.size()/2;i++)//reverse
    {
        temp=a[i];
        a[i]=a[a.size()-1-i];
        a[a.size()-1-i]=temp;
    }
    for(int i=0;i<b.size()/2;i++)//reverse
    {
        temp=b[i];
        b[i]=b[b.size()-1-i];
        b[b.size()-1-i]=temp;
    }
    if(a.size()>b.size())//add up, if greater than 2, carry a number
    {
        int count=0;
        for(int i=0;i<b.size();i++)
        {
            returnarray.push_back((a[i]-'0'+b[i]-'0'+count)%2+'0');
               
                if((a[i]-'0'+b[i]-'0'+count)/2==1)
                count=1;
                else
                count=0;      
        }
        
            for(int i=b.size();i<a.size();i++)
            {
                returnarray.push_back((a[i]-'0'+count)%2+'0');
                if((a[i]-'0'+count)/2==1)
                count=1;
                else
                count=0;     
            }
            if(count==1)
            returnarray.push_back(1+'0');
        }
         else
        {
        int count=0;
        for(int i=0;i<a.size();i++)
        {
            returnarray.push_back((a[i]-'0'+b[i]-'0'+count)%2+'0');
               
                if((a[i]-'0'+b[i]-'0'+count)/2==1)
                count=1;
                else
                count=0;      
        }      
            for(int i=a.size();i<b.size();i++)
            {
                returnarray.push_back((b[i]-'0'+count)%2+'0');
                if((b[i]-'0'+count)/2==1)
                count=1;
                else
                count=0;
                
            }
            if(count==1)
            returnarray.push_back(1+'0');
            
            

        }
        for(int i=0;i<returnarray.size()/2;i++)//reverse
            {
            temp=returnarray[i];
            returnarray[i]=returnarray[returnarray.size()-1-i];
            returnarray[returnarray.size()-1-i]=temp;
            }
       return returnarray;
    
    }
};
