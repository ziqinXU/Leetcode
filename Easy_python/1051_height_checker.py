class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        A=sorted(heights)
        count=0
        for i in range(len(heights)):
            if heights[i]!=A[i]:
                count=count+1
        return count
