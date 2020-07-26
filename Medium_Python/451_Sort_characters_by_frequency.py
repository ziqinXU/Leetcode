class Solution:
    def frequencySort(self, s: str) -> str:
        dicts=Counter(s)
        s=""
        newdict=sorted(dicts.items(),reverse=True,key=lambda k:k[1])
        for i in newdict:
            s=s+i[0]*i[1]
        return s
