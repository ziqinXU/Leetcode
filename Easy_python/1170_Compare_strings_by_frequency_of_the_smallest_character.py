class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        returnlist=[]
        lenqueries=[]
        lenwords=[]
        for i in range(len(queries)):
            sortedque=sorted(queries[i])
            A=Counter(sortedque)
            lenqueries.append(A[sortedque[0]])
        for i in range(len(words)):
            sortedwords=sorted(words[i])
            B=Counter(sortedwords)
            lenwords.append(B[sortedwords[0]])
        for i in range(len(lenqueries)):
            count=0
            for j in range(len(lenwords)):
                if lenqueries[i]<lenwords[j]:
                    count=count+1
            returnlist.append(count)
        return returnlist
