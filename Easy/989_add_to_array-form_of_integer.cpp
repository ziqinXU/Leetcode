class Solution {
public:
    vector<int> addToArrayForm(vector<int>& A, int K) {
        vector<int>Kvec;
        vector<int>returnarray;
        while(K/10!=0)
        {
            Kvec.push_back(K%10);
            K=K/10;
        }
        Kvec.push_back(K%10);
        int temp;
        for(int i=0;i<A.size()/2;i++)
        {
            temp=A[i];
            A[i]=A[A.size()-1-i];
            A[A.size()-1-i]=temp;
        }
        
        int count=0;
        if(Kvec.size()<A.size())
        {
            for(int i=0;i<Kvec.size();i++)
            {
                returnarray.push_back((A[i]+Kvec[i]+count)%10);
                if((A[i]+Kvec[i]+count)/10==1)
                count=1;
                else
                count=0;
            }

            for(int i=Kvec.size();i<A.size();i++)
            {
                returnarray.push_back((A[i]+count)%10);
                if((A[i]+count)/10==1)
                count=1;
                else
                count=0;
                
                
                
            }
            if(count==1)
            returnarray.push_back(1);
        }
        else
        {
            for(int i=0;i<A.size();i++)
            {
                returnarray.push_back((A[i]+Kvec[i]+count)%10);
                //printf("%d ",A[i]+Kvec[i]+count);
                if((A[i]+Kvec[i]+count)/10==1)
                count=1;
                else
                count=0;
               
             
               
            }

            for(int i=A.size();i<Kvec.size();i++)
            {
                returnarray.push_back((Kvec[i]+count)%10);
                if((Kvec[i]+count)/10==1)
                count=1;
                else
                count=0;
            }
            if(count==1)
            returnarray.push_back(1);
        }
        for(int i=0;i<returnarray.size()/2;i++)
        {
            temp=returnarray[i];
            returnarray[i]=returnarray[returnarray.size()-1-i];
            returnarray[returnarray.size()-1-i]=temp;
        }
        return returnarray;
    }
};
