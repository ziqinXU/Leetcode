
class Solution:
    def titleToNumber(self, s: str) -> int:
        sumarr=0
        for idx,char in enumerate(s):
            sumarr=sumarr+(ord(char)-64)*pow(26,len(s)-idx-1)
        return sumarr
