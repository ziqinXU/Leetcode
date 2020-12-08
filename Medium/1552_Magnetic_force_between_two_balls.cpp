class Solution {
public:
    //贪心+二分法
    //最小距离是1，最大距离是(position.back() - position.front()) / (m - 1)
    //贪心算法，每个点和之前的距离若大于mid，则放入，若放入总个数超过了m，说明都能放下
    bool check(int mid, vector<int> position,int m)
    {
        int pre = position[0];
        int count = 1;
        for(int i = 1; i < position.size(); i++)
        {
            if(position[i]-pre>=mid)
            {
                pre = position[i];
                count++;
            }
        }
        return count>=m;

    }
    int maxDistance(vector<int>& position, int m) {
        int res = 0;

        sort(position.begin(),position.end());
        int left = 1, right = (position.back()-position[0])/(m-1);
        while(left<=right)
        {
            int mid = left + (right - left)/2;
            if(check(mid,position,m))//if valid
            {
                res = mid;
                left = mid + 1;
            }
            else
            {
                right = mid - 1;
            }

        }
        return res;
    
    }
};
