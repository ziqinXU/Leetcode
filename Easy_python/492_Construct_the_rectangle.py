class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        W=int(sqrt(area))
        
        while True:
            print(W)
            if area%W==0:
                return [int(area/W),W]
            W=W-1
