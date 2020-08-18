class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        returnlist=[]
        p=sorted(p)
        dictP=Counter(p)
        tempstring=s[0:len(p)]
        dictS=Counter(tempstring)
        if dictS==dictP:
            returnlist.append(0)
        for i in range(1,len(s)-len(p)+1):
            dictS[s[i-1]]-=1
            if dictS[s[i-1]]==0:
                del dictS[s[i-1]]
            if s[i+len(p)-1] in dictS:
                dictS[s[i+len(p)-1]]+=1
            else:
                dictS[s[i+len(p)-1]]=1
            #print(dictS,dictP)
            if dictS==dictP:
                returnlist.append(i)

        return returnlist

