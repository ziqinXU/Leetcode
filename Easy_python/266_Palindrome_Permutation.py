class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        A=Counter(s)
        count=0
        for i in A:
            if A[i]%2==1:
                count=count+1
        if count>1:
            return False
        else:
            return True
        
