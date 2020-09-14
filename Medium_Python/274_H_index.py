class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations=sorted(citations,reverse=True)
        h=len(citations)
        i=0
        pos=0
        while h>=0:
            for i in range(pos,len(citations)):
                if citations[i]<h:
                    i=i
                    break
            if i==len(citations)-1 and citations[i]>=h:
                i=i+1
            pos=i
            #if i==len(citations)-1 and h>pos:
             #   return i+1
            #print(i)
            if h<=pos:
                return h
            else:
                h-=1
