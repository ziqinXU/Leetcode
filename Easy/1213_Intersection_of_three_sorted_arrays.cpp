class Solution {
public:
    vector<int> arraysIntersection(vector<int>& arr1, vector<int>& arr2, vector<int>& arr3) {
        //如果三个指针指向的值相等，那么三个指针同时后移
        //如果不相等，那么找最小的数，相应的指针后移
        int i=0,j=0,k=0;
        vector<int> res;
        while(i < arr1.size() && j < arr2.size() && k < arr3.size())
        {
            int a = arr1[i];
            int b = arr2[j];
            int c = arr3[k];
            if(arr1[i] == arr2[j] && arr2[j] == arr3[k])
            {
                res.push_back(arr1[i]);
                i++;
                j++;
                k++;
            }
            else
            {
                int least = min(min(arr1[i], arr2[j]), arr3[k]);
                if (arr1[i] == least) i++;
                if (arr2[j] == least) j++;
                if (arr3[k] == least) k++;

            }
        }
        return res;
    }
};
