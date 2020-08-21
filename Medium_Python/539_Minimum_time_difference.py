#统一转换为分钟后排序
class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        minutelist=[]
        for i in range(len(timePoints)):
            hour,minute=map(int,timePoints[i].split(":"))
            minutelist.append(hour*60+minute)
        minutelist=sorted(minutelist)
        mindis=2000
        for i in range(1,len(minutelist)):
            if minutelist[i]-minutelist[i-1]<mindis:
                mindis=minutelist[i]-minutelist[i-1]
        if 1440-(minutelist[-1]-minutelist[0])<mindis:
            mindis=1440-(minutelist[-1]-minutelist[0])
        return mindis
