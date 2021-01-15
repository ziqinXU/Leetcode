class Solution {
public:
    int find(int x,map<int,int>& parent) {
        if (x != parent[x]) {
            parent[x] = find(parent[x],parent);
        }
        return parent[x];
    }
    void checkunion(int x, int y, map<int,int>& parent)
    {
        int xroot = find(x,parent);
        int yroot = find(y,parent);
        if(xroot == yroot)
        {
            return;
        }
        parent[xroot] = yroot;
    }
    int removeStones(vector<vector<int>>& stones) {
        map<int,int> parent;
        for(int i = 0; i < stones.size();i++)
        {
            if(parent.find(stones[i][0])==parent.end())
            {
                parent[stones[i][0]] = stones[i][0];
            }
            if(parent.find(stones[i][1]+10000)==parent.end())
            {
                parent[stones[i][1]+10000] = stones[i][1]+10000;
            }
        }
        for(int i = 0;i < stones.size();i++)
        {
            checkunion(stones[i][0],stones[i][1]+10000,parent);
        }
        set<int>newset;
        for(map<int,int>::iterator it = parent.begin();it!=parent.end();it++)
        {
            newset.insert(find(it->first,parent));
        }
    return stones.size()-newset.size();
    }
};
