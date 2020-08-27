#N=1 K；N=2 K*K; N=3 f[i]=f[i-1]*(k-1)+f[i-2]*1*(k-1) n与n-1不同+n与n-1相同，n有K-1选择，n-1只有一种选择，即与n同
class Solution:
    def numWays(self, n: int, k: int) -> int:
        f=[0]*n
        if n==0:
            return 0
        if n==1:
            return k
        if n==2:
            return k*k
        f[0]=k
        f[1]=f[0]*k
        for i in range(2,n):
            f[i]=f[i-1]*(k-1)+f[i-2]*1*(k-1)
        return f[-1]
