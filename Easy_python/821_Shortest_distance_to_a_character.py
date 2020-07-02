class Solution:
    def shortestToChar(self, S: str, C: str) -> List[int]:
        returnarray=[None]*len(S)
        k=0
        k1=0
        pos=[]
        while S.find(C,k)!=-1:
            k1=S.find(C,k)
            returnarray[k1]=0
            pos.append(k1)
            k=k1+1
        #print(returnarray,pos)
        for i in range(len(S)):
            if i<pos[0]:
                returnarray[i]=abs(i-pos[0])
            if i>pos[len(pos)-1]:
                
                returnarray[i]=abs(i-pos[len(pos)-1])
            for j in range(len(pos)-1):
                if i > pos[j] and i < pos[j+1]:
                    returnarray[i]=min(abs(i-pos[j]),abs(i-pos[j+1]))
        return returnarray
