class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dict1={}
        dict2={}
        for i in range(len(s)):
            if s[i] in dict1:
                if t[i]!=dict1[s[i]]:
                    return False
            dict1[s[i]]=t[i]
        for i in range(len(t)):
            if t[i] in dict2:
                if s[i]!=dict2[t[i]]:
                    return False
            dict2[t[i]]=s[i]
        return True
