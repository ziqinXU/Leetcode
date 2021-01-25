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
    void checkunion(int x, int y, vector<int>& parent,vector<int>& rank)
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
                parent[y_root] =x_root;
            }
            else
            {
                rank[x_root]++;
                parent[y_root] = x_root;
            }
        }

    }
    int regionsBySlashes(vector<string>& grid) {
        int n = grid.size();
        vector<int> parent (n*n*4,-1);
        vector<int> rank(n*n*4,0);
        for(int i = 0; i < n; i++)
        {
            string cur = grid[i];
            for(int j = 0; j < n; j++)
            {
                if(cur[j] == '\\')//01 23
                {
                    checkunion(4*(i*n+j),4*(i*n+j)+1,parent,rank);
                    checkunion(4*(i*n+j)+2,4*(i*n+j)+3,parent,rank);
                }
                else if (cur[j] == '/')// 03 12
                {
                    checkunion(4*(i*n+j),4*(i*n+j)+3,parent,rank);
                    checkunion(4*(i*n+j)+1,4*(i*n+j)+2,parent,rank);
                }
                else// 01 12 23
                {
                    checkunion(4*(i*n+j),4*(i*n+j)+1,parent,rank);
                    checkunion(4*(i*n+j)+1,4*(i*n+j)+2,parent,rank);
                    checkunion(4*(i*n+j)+2,4*(i*n+j)+3,parent,rank);
                }
                //right,down
                if (j + 1 < n) 
                {
                    checkunion(4*(i*n+j)+1,4*(i*n+j)+4+3,parent,rank);
                }
                if (i + 1 < n) {
                    checkunion(4*(i*n+j)+2,4*((i+1)*n+j),parent,rank);
                }

            }
        }
        int res;
        set<int> count;
        for(int k = 0; k < 4*n*n;k++)
        {
            count.insert(find(k,parent));
        }
        return count.size();
    }
};
