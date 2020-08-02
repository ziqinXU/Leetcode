class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        returnlist=[0]*len(s)
        for i in range(len(indices)):
            returnlist[indices[i]]=s[i]
        return "".join(returnlist)
