class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        #先对区间按开始时间进行排序，若下一个开始时间小于上一个结束时间，则合并两个区间，否则添加新的区间
        #注意合并时候的右边边界
        res=[]
        if len(intervals)==0:
            return res
        intervals.sort(key=lambda x: x[0])
        res.append(intervals[0])
        for i in range(1,len(intervals)):
            if intervals[i][0]>res[-1][1]:
                res.append(intervals[i])
            else:
                res[-1][1]=max(intervals[i][1],res[-1][1])
        return res
             
