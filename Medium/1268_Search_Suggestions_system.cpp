///first attempt 40.84%faster, 100%less memory
//Idea:sort the vector with ascending order, each time, add one more alphabet in searchword, compare it with strings in products.
//save the first three in returnarray.
class Solution {
public:
    vector<vector<string>> suggestedProducts(vector<string>& products, string searchWord) {
        sort(products.begin(),products.end());
        vector<vector<string> >returnarray;
        vector<string>temparray;
        int t=1;
        while(t<=searchWord.size())//find all prefix for searchword
        {
            string compare=searchWord.substr(0,t);
            int count=0;
            
            for(int i=0;i<products.size();i++)
            {
                if(products[i].find(compare)==0)//if found products,save it
                {
                    temparray.push_back(products[i]);
                    count++;
                }
                if(count==3)//if three words are found, break;
                break;
            }
            returnarray.push_back(temparray);
            temparray.clear();
            t++;
        }
        return returnarray;
    }
};
