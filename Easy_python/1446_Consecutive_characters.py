class Solution:
    def maxPower(self, s: str) -> int:
        current=s[0]
        maxlen=0
        currentlen=0
        for i in range(len(s)):
            currentlen=0
            current=s[i]
            while i<len(s) and s[i]==current:
                currentlen=currentlen+1
                i=i+1
            if currentlen>maxlen:
                maxlen=currentlen
            
        return maxlen
                
