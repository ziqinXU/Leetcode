class Solution:
    def longestPalindrome(self, s: str) -> str:
        maxlen=1
        if len(s)==0:
            return ""
        tempstring=s[0]
        for i in range(len(s)):
            left,right=i-1,i+1
            while left>=0 and right<len(s):
                if s[left]!=s[right]:
                    break
                else:
                    left-=1
                    right+=1
            
            if right-left-1>maxlen:
                maxlen=right-left-1
                tempstring=s[left+1:right]
            left,right=i-1,i+2
            if i+1<len(s) and s[i]==s[i+1]:
                while left>=0 and right<len(s):
                    if s[left]!=s[right]:
                        break
                    else:
                        left-=1
                        right+=1
                if right-left-1>maxlen:
                    maxlen=right-left-1
                    tempstring=s[left+1:right]
        return tempstring


