class Solution:
    def minSteps(self, s: str, t: str) -> int:
        Scount=Counter(s)
        Tcount=Counter(t)
        number=0
        for i in Scount:
            if i not in Tcount:
                number=number+Scount[i]
            elif Scount[i]>Tcount[i]:
                number=number+(Scount[i]-Tcount[i])
        return number
