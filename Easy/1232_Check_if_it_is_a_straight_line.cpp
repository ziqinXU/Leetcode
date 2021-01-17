class Solution {
public:
    bool checkStraightLine(vector<vector<int>>& coordinates) {
        int x = coordinates[1][0]-coordinates[0][0];
        int y = coordinates[1][1]-coordinates[0][1];
        for(int i = 2;i < coordinates.size();i++)
        {
            int newx = coordinates[i][0]-coordinates[0][0];
            int newy = coordinates[i][1]-coordinates[0][1];
            if(newx*(-y)+newy*x!=0)
            return false;
        }
        return true;
    }
};
