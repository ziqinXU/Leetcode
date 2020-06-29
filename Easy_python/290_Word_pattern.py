class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        patternlist=list(pattern)
        strlist=str.split()
        dict1={}
        dict2={}
        if len(patternlist)!=len(strlist):
            return False
        for i in range(len(patternlist)):
            if patternlist[i] in dict1 and dict1[patternlist[i]]!=strlist[i]:
                return False
            dict1[patternlist[i]]=strlist[i]
        for i in range(len(strlist)):
            if strlist[i] in dict2 and dict2[strlist[i]]!=patternlist[i]:
                return False
            dict2[strlist[i]]=patternlist[i]
        return True
