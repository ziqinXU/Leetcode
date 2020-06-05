class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        last=0
        abssum=0
        for alphabet in word:
            current=keyboard.find(alphabet)
            abssum=abssum+abs(current-last)
            last=current
        return abssum
