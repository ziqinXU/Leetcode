class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        #贪心，可证明为最优解
        
        if k<=3:
            return 1
        F=[1,1,2]
        
        i=3
        while F[-1]<k:
            F.append(F[i-1]+F[i-2])
            i+=1
        count=0
        f=i-1
        while k!=0:
            if F[f]>k:
                f-=1
            else:
                k-=F[f]
                count+=1
        return count
            
