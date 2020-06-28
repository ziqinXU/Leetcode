class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        laststring=s
        

        for i in range(0,len(s),2*k):
            tempstring=laststring[i:i+k]
            tempstring=tempstring[::-1]
            print(laststring[:i],tempstring,laststring[i+k:])
            laststring=laststring[:i]+tempstring+laststring[i+k:]

        return laststring


