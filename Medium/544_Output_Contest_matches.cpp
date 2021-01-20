class Solution {
public:
   
string findContestMatch(int n) {
       vector<string> arr;
       for(int i = 0; i< n; i++)
       {
           arr.push_back(to_string(i+1));
       }
       int times = log2(n);

       while(times>0)
       {
            for(int j = 0; j < pow(2,times)/2;j++)
            {
                string temp;
                temp = "(" + arr[j] + "," + arr[pow(2,times)-j-1] + ")";
                arr[j] = temp;
            }
            times--;
       }
       return arr[0];
    }
};
