class Solution:
    def reverseWords(self, s: str) -> str:
        start=0
        newarray=""
        for idx,word in enumerate(s):
            if word==' ':
                end = idx
                tempstring=s[start:end]
                newarray = newarray+tempstring[::-1]
                newarray= newarray+' '
                start=idx+1
        tempstring=s[start:len(s)]
        newarray = newarray+tempstring[::-1]
        return newarray
