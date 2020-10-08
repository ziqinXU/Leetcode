class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        minval=max(weights)
        maxval=sum(weights)
        left,right=minval,maxval
        res=[]
        while left<=right:
            mid=left+(right-left)//2
            i=mid
            j=0
            count=0
            while j<len(weights):
                currentsum=0
                while j<len(weights) and weights[j]+currentsum<=i:
                    currentsum=weights[j]+currentsum
                    j+=1
                count+=1
            if count<=D:
                res.append(i)
                right=mid-1
            else:
                left=mid+1
        return min(res)
