class Solution {
public:
    int find(int x, vector<int>& parent)
    {
        int x_root = x;
        while(parent[x_root]!=-1)
        {
            x_root=parent[x_root];
        }
        return x_root;
    }
    void checkunion(int x, int y, vector<int>& parent, vector<int>& rank)
    {
        int x_root = find(x,parent);
        int y_root = find(y,parent);
        if(x_root == y_root)
        {
            return;
        }
        else
        {
            if(rank[x_root]<rank[y_root])
            {
                parent[x_root] = y_root;
            }
            else if (rank[x_root]>rank[y_root])
            {
                parent[y_root] = x_root;
            }
            else
            {
                parent[x_root]=y_root;
                rank[x_root]++;
            }
        }
    }
    int makeConnected(int n, vector<vector<int>>& connections) {
        //sort(connections.begin(),connections.end());
        if (connections.size()<n-1)
        return -1;
        vector<int> parent(n,-1);
        vector<int> rank(n,0);
        for(int i = 0; i < connections.size();i++)
        {
            checkunion(connections[i][0],connections[i][1],parent,rank);
        }
        
        set<int> count;
        for(int i = 0; i< n;i++)
        {
            count.insert(find(i,parent));
        }
        return count.size()-1;
    }
};
