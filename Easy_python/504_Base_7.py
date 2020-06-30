class Solution:
    def convertToBase7(self, num: int) -> str:
        A=[]
        if num>=0:
            while int(num/7)!=0:
                A.append(num%7)
                num=int(num/7)
            A.append(num%7)
            for i in range(int(len(A)/2)):
                temp=A[i]
                A[i]=A[len(A)-1-i]
                A[len(A)-1-i]=temp
            A=[str(A[j]) for j in range(len(A))]
            return ''.join(A)
        else:
            num=-num
            while int(num/7)!=0:
                A.append(num%7)
                num=int(num/7)
            A.append(num%7)
            for i in range(int(len(A)/2)):
                temp=A[i]
                A[i]=A[len(A)-1-i]
                A[len(A)-1-i]=temp
            A=[str(A[j]) for j in range(len(A))]
            return "-"+''.join(A)
