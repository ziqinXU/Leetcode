class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        firstdis=0
        seconddis=0
        if start<=destination:
            for i in range(start,destination):
                firstdis=firstdis+distance[i]
            return min(firstdis,sum(distance)-firstdis)
        else:
            
            for i in range(destination,start):
                firstdis=firstdis+distance[i]
            
        return min(firstdis,sum(distance)-firstdis)
            
