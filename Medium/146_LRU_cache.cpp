class LRUCache {
    int totalcapa;
    list<int> Dlist;
    map<int,pair<int,list<int>::iterator> > hashmap;//key,value,pos
public:
    LRUCache(int capacity) {
        totalcapa = capacity;
    }
    
    int get(int key) {
        map<int,pair<int,list<int>::iterator> >::iterator it = hashmap.find(key);
        if(it==hashmap.end())//not found
        {
            return -1;
        }
        else
        {
            Dlist.erase(it->second.second);//push new,exchange pos
            Dlist.push_back(key);
            hashmap[key].second = (--Dlist.end());
            return it->second.first;
        }
    }
    
    void put(int key, int value) {
        map<int,pair<int,list<int>::iterator> >::iterator it = hashmap.find(key);
        if(it != hashmap.end())
        {
            hashmap[key].first = value;
            Dlist.erase(it->second.second);
            Dlist.push_back(key);
            hashmap[key].second = (--Dlist.end());
        }
        else
        {
            
            if(hashmap.size()<totalcapa)//put back and add pairs
            {
                Dlist.push_back(key);
                hashmap[key] = make_pair(value,--Dlist.end());
            }
            else
            {   
                int removed = Dlist.front();//remove first and push new
                Dlist.pop_front();
                hashmap.erase(removed);
                Dlist.push_back(key);
                hashmap[key] = make_pair(value,--Dlist.end());
            }
        }
       
    }
};

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache* obj = new LRUCache(capacity);
 * int param_1 = obj->get(key);
 * obj->put(key,value);
 */
