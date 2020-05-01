class Solution {
public:
    int numUniqueEmails(vector<string>& emails) {
        vector<string>returnarray;
        vector<string>local;
        vector<string>domain;
        string temp;
        int returnnumber;
        for(int i=0;i<emails.size();i++)
        {
            for(int j=0;j<emails[i].size();j++)
            {
                if(emails[i][j]=='+')
                break;
                if(emails[i][j]=='@')
                break;
                if(emails[i][j]!='.'&&emails[i][j]!='+'&&emails[i][j]!='@')
                {
                    
                    temp.push_back(emails[i][j]);
                    
                }
                
            }
            local.push_back(temp);
            temp.clear();

             
        }
        
        for(int i=0;i<emails.size();i++)
        {
            for(int j=0;j<emails[i].size();j++)
            {
                if(emails[i][j]=='@')
                {
                    domain.push_back(emails[i].substr(j,emails[i].size()-j));
                }
            }
             
        }
        for(int i=0;i<emails.size();i++)
        {
            local[i].append(domain[i]);
        }
        
        int number[1000]={0};
        int p=1;
        for(int i=0;i<emails.size();i++)
        {
            if(number[i]==0)
            {
            number[i]=p;
            for(int j=i+1;j<emails.size();j++)
            {
                if(local[i]==local[j])
                {
                    number[j]=p;
                   // printf("%d %d.   ",i,j);
                }
            }
            p++;
            }
        }
       

        return p-1;
    }
};
