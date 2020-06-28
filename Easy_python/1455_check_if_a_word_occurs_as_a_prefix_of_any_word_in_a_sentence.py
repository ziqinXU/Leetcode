class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        wordlist=[]
        first=0
        for i in range(len(sentence)):
            if sentence[i]==' ':
                wordlist.append(sentence[first:i])
                first=i+1
        wordlist.append(sentence[first:])
        for i in range(len(wordlist)):
            if wordlist[i].find(searchWord)==0:
                return i+1
        return -1   

