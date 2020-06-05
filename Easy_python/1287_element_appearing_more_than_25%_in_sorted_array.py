class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        for number in arr:
            if arr.count(number)>len(arr)/4:
                return number
