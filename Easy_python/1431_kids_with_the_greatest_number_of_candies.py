class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxvalue = max(candies)
        returnjudge=[]
        for value in candies:
            if value + extraCandies>=maxvalue:
                returnjudge.append(True)
            else:
                returnjudge.append(False)
        return returnjudge
