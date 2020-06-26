class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        returnlist=[]
        for i in range(len(words)):
            for j in range(len(words)):
                if i!=j and words[j].find(words[i])!=-1:
                    returnlist.append(words[i])
        returnlist=list(set(returnlist))
        return returnlist
