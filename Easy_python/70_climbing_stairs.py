class Solution:
    def climbStairs(self, n: int) -> int:
        methods = [0]*(n)
        if n==1:
            return 1
        else:
            methods[0]=1
            methods[1]=2
            for i in range(2,n):
                #print(methods)
                methods[i] = methods[i-1] + methods[i-2]
            return methods[-1]
