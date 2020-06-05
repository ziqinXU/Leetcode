class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        count=0
        for idx in range(len(endTime)):
            if startTime[idx]<=queryTime and endTime[idx]>=queryTime:
                count=count+1
        return count
