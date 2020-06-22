class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        sumshift=0
        for i in range(len(shift)):
            if shift[i][0]==0:
                sumshift=sumshift-shift[i][1]
            else:
                sumshift=sumshift+shift[i][1]
        sumshift=sumshift%len(s)
        if sumshift>0:
            return s[-sumshift:]+s[0:len(s)-sumshift]
        if sumshift<0:
            return s[abs(sumshift):]+s[0:abs(sumshift)]
        if sumshift==0:
            return s


            
