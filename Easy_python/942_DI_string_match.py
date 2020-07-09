class Solution:
    def diStringMatch(self, S: str) -> List[int]:
        #如果当前位置为I，插入剩下index中最小数，为D则插入剩下中最大数
        returnlist=[]
        indexlist=[i for i in range(len(S)+1)]
        for i in range(len(S)):
            if S[i]=='D':
                returnlist.append(indexlist[len(indexlist)-1])
                del indexlist[len(indexlist)-1]
            if S[i]=='I':
                returnlist.append(indexlist[0])
                del indexlist[0]
        returnlist.append(indexlist[0])
        return returnlist
