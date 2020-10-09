class Solution:
    def longestRepeatingSubstring(self, S: str) -> int:
        for i in reversed(range(1,len(S))):
            hashdict=set()
            for j in range(0,len(S)-i+1):
                if S[j:j+i] not in hashdict:
                    hashdict.add(S[j:j+i])
                else:
                    return i
        return 0
