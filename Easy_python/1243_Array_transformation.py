class Solution:
    def transformArray(self, arr: List[int]) -> List[int]:
        last=arr
        current=last[:]
        while True:
            for i in range(1,len(last)-1):
                if last[i-1]<last[i] and last[i+1]<last[i]:
                    current[i]=last[i]-1
                    continue
                if last[i-1]>last[i] and last[i+1]>last[i]:
                    current[i]=last[i]+1
            if current==last:
                break
            last=current[:]

        return current
