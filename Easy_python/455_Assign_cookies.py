class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g=sorted(g)
        s=sorted(s)
        count=0
        i=0
        j=0
        while i!=len(g) and j!=len(s):
            if g[i]<=s[j]:
                count=count+1
                i=i+1
                j=j+1
            else:
                j=j+1
        return count
