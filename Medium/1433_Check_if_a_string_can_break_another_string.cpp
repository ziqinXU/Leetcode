///first attempt 50.53%faster, 100%less memory
//Idea:sort two strings, check if the dictionary order of all position in s1 is greater than s2, and vice versa.
class Solution {
public:
    bool checkIfCanBreak(string s1, string s2) {
        sort(s1.begin(),s1.end());//sort s1 and s2
        sort(s2.begin(),s2.end());
        int count1=0,count2=0;
        for(int i=0;i<s1.size();i++)//check if the dictionary order of all position in s1 is greater than s2
        {
            if(s1[i]>s2[i])
            {
                count1++;
            }
            if(s1[i]<s2[i])//check if the dictionary order of all position in s2 is greater than s1
            {
                count2++;
            }
        }
        if(count1==0||count2==0)//all in s1 is greater than s2 or s2 is greater than s1 or all alpabets are the same, return true
        return true;
        else
        return false;
    }
};
