class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        dictionarychar={}
        dictionarywords={}
        sumlen=0
        flag=0
        for idx,alphabet in enumerate(chars):
            dictionarychar[alphabet]=chars.count(alphabet)
        for i in range(len(words)):
            for j in range(len(words[i])):
                dictionarywords[words[i][j]]=words[i].count(words[i][j])
            for k in dictionarywords:
                if k in dictionarychar and dictionarychar[k]>=dictionarywords[k]:
                    flag=0
                else:
                    flag=1
                    break
            if flag==0:
                sumlen=sumlen+len(words[i])
            flag=0
            dictionarywords.clear()
        return sumlen
