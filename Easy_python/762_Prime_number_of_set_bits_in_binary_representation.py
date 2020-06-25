class Solution:
    def countPrimeSetBits(self, L: int, R: int) -> int:
        count=0
        for i in range(L,R+1):
            number=str(bin(i)).count('1')
            flag=0
            for idx in range(2, int(math.sqrt(number))+1):
                if number % idx == 0:
                    flag=1
                    break
            if flag==0 and number>=2:
                count=count+1
        return count
