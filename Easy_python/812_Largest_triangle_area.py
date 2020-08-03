class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        maxS=0
        for i in range(len(points)-2):
            for j in range(i,len(points)-1):
                for k in range(j,len(points)):
                    a=points[i]
                    b=points[j]
                    c=points[k]
                    la=math.sqrt((b[1]-a[1])**2+(b[0]-a[0])**2)
                    lb=math.sqrt((b[1]-c[1])**2+(b[0]-c[0])**2)
                    lc=math.sqrt((a[1]-c[1])**2+(a[0]-c[0])**2)
                    p=(la+lb+lc)/2
                    
                    S=math.sqrt(abs(p*(p-la)*(p-lb)*(p-lc)))#海伦公式，需要加上绝对值
                    if S>maxS:
                        maxS=S
        return maxS
