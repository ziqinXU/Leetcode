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
        while(j<arr.size()&&arr[i]==arr[j])
        {
            j++;
        }
        temp[p].first=j-i;
        temp[p].second=arr[i];
        //printf("%d %d ssss",j-i,arr[i]);
        i=j-1;
        comparearray.push_back(temp[p]);
    }
    sort(comparearray.begin(),comparearray.end());
    int sum=0;
    int k=comparearray.size()-1;
    while(arr.size()-sum>arr.size()/2+arr.size()%2)
    {
        sum=sum+comparearray[k].first;
        
        k--;
    }

    return comparearray.size()-k-1;

       
    }
};
