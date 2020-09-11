class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        dict1={}
        dict2={}
        res=[]
        for j in range(len(words)):
            word=words[j]
            found1=1
            for i in range(len(pattern)):
                if pattern[i] not in dict1:
                    dict1[pattern[i]]=word[i]
                else:
                    last=dict1[pattern[i]]
                    
                    if last!=word[i]:
                        found1=0
                        break
            found2=1
            for i in range(len(pattern)):
                if word[i] not in dict2:
                    dict2[word[i]]=pattern[i]
                else:
                    last=dict2[word[i]]
                    
                    if last!=pattern[i]:
                        found2=0
                        break
                        
            if found1==1 and found2==1:
                res.append(word)
            dict1.clear()
            dict2.clear()
        return res
