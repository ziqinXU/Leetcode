class Solution:
    def largeGroupPositions(self, S: str) -> List[List[int]]:
        i=0
        returnlist=[]
        
        while i < len(S):
            start=i
            while(i+1<len(S) and S[i]==S[i+1]):
                i=i+1
            end=i
           
            if end-start>=2:
                returnlist.append([start,end])
            i=i+1
        return returnlist
