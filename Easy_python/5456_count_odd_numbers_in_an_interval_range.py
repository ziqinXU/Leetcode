class Solution:
    def countOdds(self, low: int, high: int) -> int:
        count=0
        if low%2==1 and high%2==1:
            count=count+1+int((high-low)/2)
        elif low%2==1 or high%2==1:
            count=count+1+int((high-low)/2)
        else:
            count=count+int((high-low)/2)
        return count
