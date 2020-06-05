class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        count=0
        for alphabetJ in J:
            count=count+S.count(alphabetJ)
        return count
