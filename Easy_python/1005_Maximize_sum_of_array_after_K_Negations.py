class Solution:
    def largestSumAfterKNegations(self, A: List[int], K: int) -> int:
        #1.负数>K:最小K个负数取反
        #2.负数<K:将所有负取反，如果(K-负)/2为偶数，则所有取和
        #3.负数<K:将所有负取反，如果(K-负)/2为奇数，则现有数列中最小的取反后求和
        newA=sorted(A)
        for i in range(len(newA)):
            if newA[i]>=0:
                pos=i
                break
        if pos>K:
            return -sum(newA[:K])+sum(newA[K:])
        else:
            if (K-pos)%2==0:
                return -sum(newA[:pos])+sum(newA[pos:])
            else:
                for i in range(pos):
                    newA[i]=-newA[i]
                newA=sorted(newA)
                newA[0]=-newA[0]
                return sum(newA)


