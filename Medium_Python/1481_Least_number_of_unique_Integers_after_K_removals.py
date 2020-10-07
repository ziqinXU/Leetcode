class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        arrdict=Counter(arr)
        newdict={k:v for k,v in sorted(arrdict.items(),key=lambda item:item[1])}
        total=len(newdict)
        count=0
        for i in newdict:
            if k-newdict[i]>=0:
                k=k-newdict[i]
                count+=1
        return total-count

