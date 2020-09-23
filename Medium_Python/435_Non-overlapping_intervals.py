class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        #和最长上升子序列思想相同，先排序，后去除,考虑空的情况，注意要break
        if len(intervals)==0:
            return 0
        intervals.sort(key=lambda k:k[0])
        dp=[0]*len(intervals)
        for i in range(len(intervals)):
            dp[i]=1
            for j in reversed(range(0,i)):
                if intervals[i][0]>=intervals[j][1]:
                    dp[i]=max(dp[i],dp[j]+1)
                    break
        return len(intervals)-max(dp)
