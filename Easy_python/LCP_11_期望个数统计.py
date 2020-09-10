#求有多少个不重复的数字
class Solution:
    def expectNumber(self, scores: List[int]) -> int:
        return len(set(scores))
