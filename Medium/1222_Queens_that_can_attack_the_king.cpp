///first attempt 92.72%faster, 100%less memory
//Idea:find the position of the king, and search the first queen in its horizontal, vertical and diagonal directions.
class Solution {
public:
    vector<vector<int>> queensAttacktheKing(vector<vector<int>>& queens, vector<int>& king) {
        vector<vector<int>> returnarray;
        vector<int>temp;
        int intarray[9][9];
        for(int i=0;i<9;i++)//mark the positions of the queen
        {
            for(int j=0;j<9;j++)
            {
                intarray[i][j]=0;
            }
        }
        for(int i=0;i<queens.size();i++)
        {
            intarray[queens[i][0]][queens[i][1]]=1;
        }
        int i=king[0]-1;
        while(i>=0)//search the upper part
        {
            if(intarray[i][king[1]]==1)
            {
                temp.push_back(i);
                temp.push_back(king[1]);
                returnarray.push_back(temp);
                temp.clear();
                break;
            }
            i--;
        }
        i=king[0]+1;
        while(i<9)//search the lower part
        {
            if(intarray[i][king[1]]==1)
            {
                temp.push_back(i);
                temp.push_back(king[1]);
                returnarray.push_back(temp);
                temp.clear();
                break;
            }
            i++;
        }
        int j=king[1]-1;
        while(j>=0)//search the left part
        {
            if(intarray[king[0]][j]==1)
            {
                temp.push_back(king[0]);
                temp.push_back(j);
                returnarray.push_back(temp);
                temp.clear();
                break;
            }
            j--;
        }
        j=king[1]+1;
        while(j<9)//search the right part
        {
            if(intarray[king[0]][j]==1)
            {
                temp.push_back(king[0]);
                temp.push_back(j);
                returnarray.push_back(temp);
                temp.clear();
                break;
            }
            j++;
        }
        i=king[0]-1;
        j=king[1]-1;
        while(i>=0&&j>=0)//search the upperleft
        {
            if(intarray[i][j]==1)
            {
                temp.push_back(i);
                temp.push_back(j);
                returnarray.push_back(temp);
                temp.clear();
                break;
            }
            i--;
            j--;
        }
        i=king[0]+1;
        j=king[1]+1;
        while(i<9&&j<9)
        {
            if(intarray[i][j]==1)
            {
                temp.push_back(i);
                temp.push_back(j);
                returnarray.push_back(temp);
                temp.clear();
                break;
            }
            i++;
            j++;
        }
        i=king[0]-1;
        j=king[1]+1;
        while(i>=0&&j<9)
        {
            if(intarray[i][j]==1)
            {
                temp.push_back(i);
                temp.push_back(j);
                returnarray.push_back(temp);
                temp.clear();
                break;
            }
            i--;
            j++;
        }
        i=king[0]+1;
        j=king[1]-1;
        while(j>=0&&i<9)
        {
            if(intarray[i][j]==1)
            {
                temp.push_back(i);
                temp.push_back(j);
                returnarray.push_back(temp);
                temp.clear();
                break;
            }
            i++;
            j--;
        }
        return returnarray;
    }
};
