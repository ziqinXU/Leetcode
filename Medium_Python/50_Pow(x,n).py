#分治思想，递归
class Solution:
    def myPow(self, x: float, n: int) -> float:
        def calPowpos(x,n):
            if n==0:
                return 1
            if n%2==0:
                y=calPowpos(x,n/2)
                return y*y
            else:
                y=calPowpos(x,(n-1)/2)
                return y*y*x
        def calPowneg(x,n):
            if n==-1:
                return float(1/x)
            if n%2==0:
                y=calPowneg(x,n/2)
                return y*y
            else:
                y=calPowneg(x,(n+1)/2)
                return y*y*float(1/x)
        if n==0:
            return 1
        if n>0:
            return calPowpos(x,n)
        else:
            return calPowneg(x,n)
