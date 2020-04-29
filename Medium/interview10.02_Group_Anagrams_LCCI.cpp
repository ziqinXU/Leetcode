///first attempt 5.13% faster, 100%less memory
//Idea:sort each string with acsend order and compare them, pick the same string out and group them.
class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        vector<vector<string> >returnarray;
        vector<string>temparray;
        vector<string>temp;
        //string tempstring;
        for(int i=0;i<strs.size();i++)
        {
            temparray.push_back(strs[i]);//use temp vector to save original strings.
        }
        for(int i=0;i<strs.size();i++)
        {
            sort(strs[i].begin(),strs[i].end());//sort each string
        }
        int arr[100000]={0};
        int p=1;
        int found;
        for(int i=0;i<strs.size();i++) //label the same string with same number
        {
            found=0;
            if(arr[i]==0)
            {
            for(int j=i+1;j<strs.size();j++)
            {
                if(strs[i]==strs[j]&&arr[j]==0)
                {
                    arr[i]=p;
                    arr[j]=p;
                    found=1;
                }
            }
            if(found==0)
            {
                arr[i]=p;
                p++;
            }
            else
            p++;
            }
        }
        /*for(int i=0;i<strs.size();i++)
        {
           printf("%d ",arr[i]);
        }*/
        for(int i=0;i<strs.size();i++) //group the string with same label
        {
            
            if(arr[i]!=-1)
            {
                temp.push_back(temparray[i]);
                for(int j=i+1;j<strs.size();j++)
                {
                    
                    if(arr[i]==arr[j])
                    {
                        temp.push_back(temparray[j]);
                        arr[j]=-1;
                    }
                    
                    
                }
                returnarray.push_back(temp);
                temp.clear();
            }
        }
        return returnarray;

    }
};
