class Solution:
    def distributeCandies(self, candies: List[int]) -> int:
        A=Counter(candies)
        if int(len(candies)/2)>=len(A):
            return len(A)
        else:
            return int(len(candies)/2)
        
