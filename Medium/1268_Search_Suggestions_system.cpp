class Solution {
public:
    vector<vector<string>> suggestedProducts(vector<string>& products, string searchWord) {
        sort(products.begin(),products.end());
        vector<vector<string> >returnarray;
        vector<string>temparray;
        int t=1;
        while(t<=searchWord.size())
        {
            string compare=searchWord.substr(0,t);
            int count=0;
            
            for(int i=0;i<products.size();i++)
            {
                if(products[i].find(compare)==0)
                {
                    temparray.push_back(products[i]);
                    count++;
                }
                if(count==3)
                break;
            }
            returnarray.push_back(temparray);
            temparray.clear();
            t++;
        }
        return returnarray;
    }
};
