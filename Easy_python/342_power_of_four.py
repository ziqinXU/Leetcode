class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        if num<=0:
            return False
        else:
            while num%4==0:
                num=int(num/4)
            if num==1:
                return True
            else:
                return False
