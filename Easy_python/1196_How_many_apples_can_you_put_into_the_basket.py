class Solution:
    def maxNumberOfApples(self, arr: List[int]) -> int:
        #尽可能多的苹果=选择重量轻的
        newarr=sorted(arr)
        arrsum=0
        for i in range(len(newarr)):
            arrsum=arrsum+newarr[i]
            if arrsum>5000:
                return i
        return i+1
