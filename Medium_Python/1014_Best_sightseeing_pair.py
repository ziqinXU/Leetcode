#A[i]+i A[j]-j,遍历经过每个j时，加上当前元素前所有数的最大值
class Solution:
    def maxScoreSightseeingPair(self, A: List[int]) -> int:
        maxsum=0
        maxvalue=A[0]+0
        for i in range(1,len(A)):
            if A[i]-i+maxvalue>maxsum:
                maxsum=A[i]-i+maxvalue
            if A[i]+i>maxvalue:
                maxvalue=A[i]+i
        return maxsum
