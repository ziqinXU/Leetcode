class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        A = sorted(target)
        B = sorted(arr)
        if A == B:
            return True
        else:
            return False
