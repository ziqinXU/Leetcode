class Solution {
public:
    bool isArmstrong(int N) {
        vector<int> arr;
        int number=N;
        int count=0;
        while(number/10!=0)
        {
            arr.push_back(number%10);
            number=number/10;
            count+=1;
        }
        arr.push_back(number%10);
        count+=1;
        int sum=0;
        for(int i=0; i < arr.size();i++)
        {
            sum+=pow(arr[i],count);
        }
        if(sum == N)
            return true;
        else
            return false;
    }
};
