class Solution:
    def numSplits(self, s: str) -> int:
        #左右dict
        count=0
        hashdictleft={}
        hashdictright={}
        left=s[:1]
        hashdictleft[s[0]]=1
        right=s[1:]
        for i in range(len(right)):
            if right[i] in hashdictright:
                hashdictright[right[i]]=hashdictright[right[i]]+1
            else:
                hashdictright[right[i]]=1
        if len(hashdictleft)==len(hashdictright):
            count=count+1
        #print(hashdictleft,hashdictright)
        for i in range(1,len(s)):
            if s[i] in hashdictleft:
                hashdictleft[s[i]]=hashdictleft[s[i]]+1
            else:
                hashdictleft[s[i]]=1
            
            hashdictright[s[i]]=hashdictright[s[i]]-1
            if hashdictright[s[i]]==0:
                del hashdictright[s[i]]
            #print(hashdictleft,hashdictright)
            if len(hashdictleft)==len(hashdictright):
                count=count+1
        return count
