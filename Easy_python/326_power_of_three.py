class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n<=0:
            return False
        else:
            while n%3==0:
                n=int(n/3)
            if n==1:
                return True
            else:
                return False
