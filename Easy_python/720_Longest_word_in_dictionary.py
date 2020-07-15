class Solution:
    def longestWord(self, words: List[str]) -> str:
        A=sorted(words)
        returnlist=[]
        maxlen=0
        print(A)
        for i in range(len(words)):
            flag=0
            for j in range(1,len(A[i])):
                if A[i][:j] not in words:
                    flag=1
            if flag==0:
                returnlist.append(A[i])
                if len(A[i])>maxlen:
                    maxlen=len(A[i])


        for i in range(len(returnlist)):
            if len(returnlist[i])==maxlen:
                return returnlist[i]
