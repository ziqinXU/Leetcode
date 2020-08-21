用stack，FIFO
class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        stack=list()
        dictword={}
        maxlen=0
        for i in range(len(s)):
            stack.append(s[i])
            if s[i] in dictword:
                dictword[s[i]]+=1
            else:
                dictword[s[i]]=1
            while len(dictword)>2:
                tempword=stack.pop(0)
                dictword[tempword]-=1
                if dictword[tempword]==0:
                    del dictword[tempword]
            length=0
            for word in dictword:
                length=dictword[word]+length
            if length>maxlen:
                maxlen=length
        
        return maxlen
        
