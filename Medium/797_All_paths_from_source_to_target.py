class Solution {
public:
    //第一步是以节点start加入到路径，循环中是从节点START开始逐个访问START能到达的点，循环完毕之后节点v就应该pop_back()， 而循环中的findPath执行完毕也会把自己访问的点pop_back() hzx-leetcode用户题解
    vector<vector<int>> returnarray;
    vector<vector<int>> allPathsSourceTarget(vector<vector<int>>& graph) {
        vector<int> foundpath;
        dfs(0,graph,foundpath);
        return returnarray;
    }
        void dfs(int start,vector<vector<int>> graph,vector<int> foundpath)
        {
            foundpath.push_back(start);
            if(start == graph.size()-1) 
            returnarray.push_back(foundpath);
            for(auto nodes: graph[start])
            {
                dfs(nodes, graph, foundpath);
            }
            foundpath.pop_back(); 
        }
    
};
