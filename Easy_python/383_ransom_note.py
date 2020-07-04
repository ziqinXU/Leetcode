class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        A=Counter(ransomNote)
        B=Counter(magazine)
        for i in A:
            if B[i]<A[i]:
                return False
        return True
        
