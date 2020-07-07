class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        sentence="".join(s)
        words=sentence.split()
        words=words[::-1]
        words=" ".join(words)
        for i in range(len(s)):
            s[i]=words[i]
        
