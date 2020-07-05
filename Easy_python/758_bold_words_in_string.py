class Solution:
    def boldWords(self, words: List[str], S: str) -> str:
        bold=[0]*len(S)
        for i in range(len(words)):
            k=0
            k1=0
            while S.find(words[i],k)!=-1:
                k1=S.find(words[i],k)
                k=k1+1
                for j in range(k1,k1+len(words[i])):
                    bold[j]=1
        i = 0

        returnarray=""
        while i<len(S):
            if bold[i]!=1:
                returnarray=returnarray+S[i]
                i=i+1
            else:
                returnarray=returnarray+"<b>"
                
                while i<len(S) and bold[i]==1:
                    returnarray=returnarray+S[i]                    
                    i=i+1
                returnarray=returnarray+"</b>"
            
        return returnarray
