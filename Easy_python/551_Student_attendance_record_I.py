class Solution:
    def checkRecord(self, s: str) -> bool:
        k=0
        k1=0
        count=0
        while s.find('A',k)!=-1:
            k1=s.find('A',k)
            k=k1+1
            count=count+1
        if count>1:
            return False
        count1=0
        k=0
        k1=0
        while s.find('LL',k)!=-1:
            k1=s.find('LL',k)
            if k1==k and k!=0:
                return False
            k=k1+1
            

        return True
        
