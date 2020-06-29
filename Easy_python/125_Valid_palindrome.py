class Solution:
    import string
    def isPalindrome(self, s: str) -> bool:
        number="0123456789"
        alphabet=string.ascii_lowercase
        s=list(s.lower())
        i=0
        while i < len(s):
            if s[i] not in number and s[i] not in alphabet:
                del s[i]
                i=i-1
            i=i+1
        for i in range(int(len(s)/2)):
            if s[i]!=s[len(s)-1-i]:
                return False
        return True

