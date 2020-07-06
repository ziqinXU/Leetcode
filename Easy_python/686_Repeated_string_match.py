class Solution:
    def repeatedStringMatch(self, A: str, B: str) -> int:
        
        if len(A)<=len(B):
            count=1
            arr=A
            while len(arr)<=len(B)+2*len(A):# A="ab" B="bababa" size(A)*(n+2)头尾各多一次
                if arr.find(B)!=-1:
                    return count
                else:
                    arr=arr+A
                    count=count+1
        else:
            count=1
            number=0
            arr=A
            while number<2:
                if arr.find(B)!=-1:
                    return count
                else:
                    arr=arr+A
                    count=count+1
                number=number+1
        return -1
