class Solution:
    def missingNumber(self, arr: List[int]) -> int:
        distance=int((arr[len(arr)-1]-arr[0])/len(arr))
        for i in range(len(arr)-1):
            if arr[i+1]-arr[i]!=distance:
                return arr[i]+distance
        return arr[i]
