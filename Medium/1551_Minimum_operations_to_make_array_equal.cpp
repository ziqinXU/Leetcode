class Solution {
public:
    int minOperations(int n) {
        if(n%2==0)
        {
            int number=int((2*n-1-n-1)/2)+1;
            return (2*n-1+n+1)*number/2-n/2*n;
        }
        else
        {
            int number=int(n/2);
            return (2*n-1+n+2)*number/2-int(n/2)*n;
        }
        
    }
};
