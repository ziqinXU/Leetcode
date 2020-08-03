class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        checkstring=[]
        i=len(str1)
        while i>=1:
            if len(str1)%i==0:
                if str1[:i]*(len(str1)//i)==str1:
                    checkstring.append(str1[:i])
            i=i-1
        for i in range(len(checkstring)):
            if len(str2)%len(checkstring[i])==0:
                if checkstring[i]*(len(str2)//len(checkstring[i]))==str2:
                    return checkstring[i]
        return ""
                    
