class Solution {
public:
    bool checkIfCanBreak(string s1, string s2) {
        sort(s1.begin(),s1.end());
        sort(s2.begin(),s2.end());
        int count1=0,count2=0;
        for(int i=0;i<s1.size();i++)
        {
            if(s1[i]>s2[i])
            {
                count1++;
                //std::cout<<count<<endl;
            }
            if(s1[i]<s2[i])
            {
                count2++;
            }
        }
        //std::cout<<count1<<endl;
        if(count1==0||count2==0)
        return true;
        else
        return false;
    }
};
