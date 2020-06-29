class Solution:
    def firstUniqChar(self, s: str) -> int:
        A=Counter(s)
        for i in range(len(s)):
            if A[s[i]]==1:
                return i
        return -1
