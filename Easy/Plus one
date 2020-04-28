class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
    int pos=digits.size()-1;
    int size=digits.size();
    if(digits[digits.size()-1]<9)
    {
        digits[digits.size()-1]++;
        return digits;
    }
    while(pos!=-1&&digits[pos]==9)
    {
        pos--;
    }
    
    if(pos!=-1)
    {
        digits[pos]++;
        for(int i=pos+1;i<digits.size();i++)
        {
            digits[i]=0;
        }
    }
    if(pos==-1)
    {
        digits.clear();
        digits.push_back(1);
        for(int i=0;i<size;i++)
        {
            digits.push_back(0);
        }
    }
    return digits;
    }
};
