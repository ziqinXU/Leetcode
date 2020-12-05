class Solution {
public:
    int leastInterval(vector<char>& tasks, int n) {
        //总排队时间 = (桶个数 - 1) * (n + 1) + 最后一桶的任务数,和总任务数中较大
        map<char,int> hashmaptasks;
        for(int i=0; i < tasks.size(); i++)
        {
            if(hashmaptasks.find(tasks[i])== hashmaptasks.end())
            {
                hashmaptasks[tasks[i]] = 1;
            }
            else
            {
                hashmaptasks[tasks[i]] += 1;
            }
        }
        int countnumber = 0;
        int maxvalue = 0;
        char alpha;
        for(map<char, int>::iterator it=hashmaptasks.begin();it!=hashmaptasks.end();++it)
        {
            
            if(it->second > maxvalue)
            {
                alpha = it->first;
                maxvalue = it->second;
            }
        }
        int lastcount = 0;
        for(map<char, int>::iterator it=hashmaptasks.begin();it!=hashmaptasks.end();++it)
        {
            
            if(it->second == maxvalue)
            {
                lastcount++;
                
            }
        }
        int tempres = (hashmaptasks[alpha]-1)*(n+1)+lastcount;
        int tasks_size = tasks.size();
        int res = max(tempres,tasks_size);
        //return tasks.size()(hashmaptasks[alpha]-1)*(n+1)+lastcount);
        return res;
    }
};
