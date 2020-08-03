class Solution:
    def rotatedDigits(self, N: int) -> int:
        good=['0','1','8']
        bad=['3','4','7']
        count=0
        for i in range(1,N+1):
            templist = list(str(i))
            flag=0
            if '2' in templist or '5' in templist or '6' in templist or '9' in templist:
                flag=1
            if '3' in templist or '4' in templist or '7' in templist:
                flag=2
            if flag==1:
                count=count+1
        return count

