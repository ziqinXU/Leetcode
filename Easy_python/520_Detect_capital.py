class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if word==word.upper():
            return True
        elif word==word.lower():
            return True
        else:
            if word[0].isupper() and word[1:]==word[1:].lower():
                return True
            else:
                return False
