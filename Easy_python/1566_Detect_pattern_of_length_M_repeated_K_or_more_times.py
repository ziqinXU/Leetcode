class Solution:
    def containsPattern(self, arr: List[int], m: int, k: int) -> bool:
        i=0
        found=0
        while i<len(arr)-k*m+1:
            temparr=arr[i:m+i]
            count=0
            #print(temparr)
            while count<k:
                if temparr!=arr[i+(count+1)*m:i+(count+2)*m]:
                    break
                count=count+1
            #print(count)
            if count==k-1:
                found=1
                break
            i=i+1
        if found==0:
            return False
        else:
            return True
