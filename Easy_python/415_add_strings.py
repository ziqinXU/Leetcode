class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        returnlist=['0']*(max(len(num1),len(num2))+1)
        if len(num1)<len(num2):
            num1=num1.zfill(len(num2)+1)
            num2=num2.zfill(len(num2)+1)
        else:
            num2=num2.zfill(len(num1)+1)
            num1=num1.zfill(len(num1)+1)
        last=0
        for i in reversed(range(len(num1))):
            
            if int(num1[i])+int(num2[i])+last>=10:
                returnlist[i]=str(int(num1[i])+int(num2[i])+last-10)
                last=1
            else:
                returnlist[i]=str(int(num1[i])+int(num2[i])+last)
                last=0
        #print(returnlist)
        if returnlist[0]=="0":
            return ''.join(returnlist[1:])
        else:
            return ''.join(returnlist)
               

