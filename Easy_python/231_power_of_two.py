class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n<=0:
            return False
        else:
            while n%2==0:
                n=int(n/2)
            if n==1:
                return True
            else:
                return False
