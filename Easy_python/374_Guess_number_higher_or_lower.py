# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        left=1
        right=n
        mid=(left+right)/2
        while guess(mid)!=0:
            mid=(left+right)/2
            if guess(mid)==-1:
                right=mid-1
            elif guess(mid)==1:
                left=mid+1

        return int(mid)
