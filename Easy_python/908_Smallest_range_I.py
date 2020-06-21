class Solution:
    def smallestRangeI(self, A: List[int], K: int) -> int:
    
        #if maximum-k - minimum+k greater than zero, return, otherwise return 0
        if (max(A)-K)-(min(A)+K)>=0:
            return (max(A)-K)-(min(A)+K)
        else:
            return 0
