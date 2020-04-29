///first attempt 22.89%faster, 100%less memory
//Idea: Save numbers in arrays with their frequency, sort the frequency and remove from the highest frequency, 
//stop when the remaining part is less or equl to the half.
class Solution {
public:
    int minSetSize(vector<int>& arr) {
    sort(arr.begin(),arr.end());
    pair<int,int>temp[100000];
    vector<pair<int,int> >comparearray;
    int p=0;
    for(int i=0;i<arr.size();i++)
    {
        int j=i+1;
        while(j<arr.size()&&arr[i]==arr[j])//count the frequency of a number
        {
            j++;
        }
        temp[p].first=j-i; //save the frequency
        temp[p].second=arr[i];//number itself
        i=j-1;
        comparearray.push_back(temp[p]);
    }
    sort(comparearray.begin(),comparearray.end());//sort with frequency (first)
    int sum=0;
    int k=comparearray.size()-1;
    while(arr.size()-sum>arr.size()/2+arr.size()%2)//if the removed part is equal to the half, stop it.
    {
        sum=sum+comparearray[k].first;
        
        k--;
    }

    return comparearray.size()-k-1;

       
    }
};
