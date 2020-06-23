class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        returnarray=[]
        returnnumber=[]
        connectedstring=first+' '+second
        k=0
        while text.find(connectedstring,k)!=-1:
            k1=text.find(connectedstring,k)
            k=k1+1
            if k1==0 or (k1-1 > 0 and k1+len(connectedstring)<len(text) and text[k1-1]==' ' and text[k1+len(connectedstring)]==' '):
                
                returnnumber.append(k1+1+len(connectedstring))
        for i in range(len(returnnumber)):
            p=returnnumber[i]
            while p<len(text) and text[p]!=' ':
                p=p+1
            returnarray.append(text[returnnumber[i]:p])
        return returnarray
        
