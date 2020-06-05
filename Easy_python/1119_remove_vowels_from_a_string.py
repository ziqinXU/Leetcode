class Solution:
    def removeVowels(self, S: str) -> str:
        Vowels=['a','e','i','o','u']
        for alphabet in Vowels:
            S=S.replace(alphabet, "")
        return S
