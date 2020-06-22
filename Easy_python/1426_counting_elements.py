class Solution:
    def countElements(self, arr: List[int]) -> int:
        count=0
        for idx, number in enumerate(arr):
            if number+1 in arr:
                count=count+1
        return count
