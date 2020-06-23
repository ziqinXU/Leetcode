class Solution:
    def numberOfLines(self, widths: List[int], S: str) -> List[int]:
        numbersum=0
        row=1
        for i in range(len(S)):
            if numbersum+widths[ord(S[i])-ord('a')]>100:
                row=row+1
                numbersum=widths[ord(S[i])-ord('a')]
            else:
                numbersum=numbersum+widths[ord(S[i])-ord('a')]
        return [row,numbersum]
            
            
