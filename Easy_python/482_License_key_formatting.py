class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        S=S.upper()
        newS=''.join(S.split('-'))
        firstlen=len(newS)%K
        parts=int(len(newS)/K)
        returnstring=""
        returnstring=returnstring+newS[:firstlen]
        pos=firstlen
        if firstlen!=0:
            if parts!=0:
                returnstring=returnstring+'-'
            for i in range(parts):
                returnstring=returnstring+newS[pos:pos+K]
                if i!=parts-1:
                    returnstring=returnstring+'-'
                pos=pos+K
                
        else:
            for i in range(parts):
                returnstring=returnstring+newS[pos:pos+K]
                if i!=parts-1:
                    returnstring=returnstring+'-'
                pos=pos+K
        return returnstring

        
