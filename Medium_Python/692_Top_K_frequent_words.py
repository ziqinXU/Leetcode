class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        wordlist=[]
        worddict={}
        for i in range(len(words)):
            if words[i] not in wordlist:
                wordlist.append(words[i])
            if words[i] not in worddict:
                worddict[words[i]]=1
            else:
                worddict[words[i]]+=1
        newdic = sorted(worddict.items(), key = lambda item: (-item[1],item[0]))
        return [i[0] for idx,i in enumerate(newdic) if idx<k]
