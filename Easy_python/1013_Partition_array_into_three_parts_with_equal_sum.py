class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        arrsum=sum(A)
        if arrsum%3!=0:
            return False
        else:
            sum1=0
            sum2=0
            sum3=0
            j=0
            k=0
            flag=0
            for i in range(len(A)):
                sum1=sum1+A[i]
                
                if sum1==arrsum/3:
                    j=i
                    flag=flag+1
                    break

            for i in range(j+1,len(A)):
                sum2=sum2+A[i]
                
                if sum2==arrsum/3:
                    k=i
                    flag=flag+1
                    break

            for i in range(k+1,len(A)):
                sum3=sum3+A[i]
                
                if sum3==arrsum/3:
                    flag=flag+1
                    break

            if sum1==arrsum/3 and sum2==arrsum/3 and sum3==arrsum/3 and flag==3:
                return True
            else:
                return False
