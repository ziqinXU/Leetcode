class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        arrsum=0
        arrmulti=1
        for char in str(n):

            arrsum=arrsum+int(char)
            arrmulti=arrmulti*int(char)
        return arrmulti-arrsum
