///first attempt 44.68%faster, 100%less memory
//Idea:Seperate odd and even part from each string and sort them, combined together again and use hashmap to count
//the different string number
class Solution {
public:
    int numSpecialEquivGroups(vector<string>& A) {
        map<string,int>hashmap;
        string tempodd;
        string tempeven;
        string temp;
        for(int i=0;i<A.size();i++)
        {
            for(int j=0;j<A[i].size();j=j+2)//save the odd position alphabets 
            {
                tempodd.push_back(A[i][j]);
            }
            for(int j=1;j<A[i].size();j=j+2)//save the even position alphabets 
            {
                tempeven.push_back(A[i][j]);
            }
            sort(tempodd.begin(),tempodd.end());//sort string and combined together
            sort(tempeven.begin(),tempeven.end());
            temp.append(tempodd);
            temp.append(tempeven);
            hashmap[temp]++;//count number of same strings
            temp.clear();
            tempodd.clear();
            tempeven.clear();
        }
        return hashmap.size();//return size of hashmap and it is also the result
    }
};
