class OrderedStream {
public:
    vector<string> stream;
    int ptr=1;
    OrderedStream(int n) {
        for(int i=0 ;i< n+2; i++)
        {
            stream.push_back("");
        }

    }
    
    vector<string> insert(int id, string value) {
        stream[id] = value;
        vector<string> res;
        
        while(stream[ptr]!="")
        {
            
            res.push_back(stream[ptr]);
            ptr++;
        }
        
        return res;
    }
};

/**
 * Your OrderedStream object will be instantiated and called as such:
 * OrderedStream* obj = new OrderedStream(n);
 * vector<string> param_1 = obj->insert(id,value);
 */
