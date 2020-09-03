class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if len(s)==0:
            return ""
        if numRows==1:
            return s
        num_groups = len(s)//((numRows-1)*2)
        rest = len(s)%((numRows-1)*2)
        if rest!=0:
            num_groups+=1
        stringmatrix=[[0]*(numRows-1)*2 for i in range(num_groups)]
        #print(num_groups,rest,stringmatrix)
        t=0
        for i in range(num_groups):
            for j in range((numRows-1)*2):
                if t<len(s):
                    stringmatrix[i][j]=s[t]
                t=t+1
        returnstring=""
        #maxi=(numRows-1)*2//2
        rows=[]
        for i in range(1,(numRows-1)*2//2+1):
            rows.append(i)
            if (numRows-1)*2-i!=i:
                rows.append((numRows-1)*2-i)

        for j in range(num_groups):
            if stringmatrix[j][0]!=0:
                returnstring+=(stringmatrix[j][0])
        
        for i in range(0,len(rows),2):
            for j in range(num_groups):
                #print(stringmatrix[j][i],j,i)
                if stringmatrix[j][rows[i]]!=0:
                    returnstring+=(stringmatrix[j][rows[i]])
                if i+1<len(rows) and stringmatrix[j][rows[i+1]]!=0:
                    returnstring+=(stringmatrix[j][rows[i+1]])
            
        return returnstring    
