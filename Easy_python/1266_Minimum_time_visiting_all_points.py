class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        #取x,y坐标差值中最大的
        timesum=0
        for i in range(len(points)-1):
            timesum=timesum+max(abs(points[i+1][1]-points[i][1]),abs(points[i+1][0]-points[i][0]))
        return timesum
