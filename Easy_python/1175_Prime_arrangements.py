class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        countprime=0
        for i in range(2,n+1):
            flag=0
            for j in range(2,int(math.sqrt(i)+1)):
                if i%j==0:
                    flag=1
                    break
            if flag==0:
                countprime=countprime+1
        return (math.factorial(countprime)*math.factorial(n-countprime))%(10**9+7)
