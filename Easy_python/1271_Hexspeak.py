class Solution:
    def toHexspeak(self, num: str) -> str:
        number=int(num)
        A=[]
        validlist=[10,11,12,13,14,15,1,0]
        numberlist=["1","0","10","11","12","13","14","15"]
        alphabetlist=["I","O","A","B","C","D","E","F"]
        while int(number/16)!=0:
            if number%16 not in validlist:
                return "ERROR"
            if number%16>=10:
                A.append(chr(65+number%16-10))
            if number%16==0:
                A.append("O")
            if number%16==1:
                A.append("I")
            number=int(number/16)
        if number%16 not in validlist:
                return "ERROR"
        if number%16>=10:
                A.append(chr(65+number%16-10))
        if number%16==0:
                A.append("O")
        if number%16==1:
                A.append("I")
        for i in range(int(len(A)/2)):
            temp=A[i]
            A[i]=A[len(A)-1-i]
            A[len(A)-1-i]=temp
        return "".join(A)
