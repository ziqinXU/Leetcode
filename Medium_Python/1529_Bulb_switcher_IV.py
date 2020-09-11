class Solution:
    def minFlips(self, target: str) -> int:
        #如果一个灯泡被翻转，则一定是选择了该灯泡的下标或者该灯泡前面的某个下标，然后进行了翻转操作，从后往前遍历
        i=len(target)-1
        count=0
        while i>=0:
            j=i
            #print(j)
            while j>=0 and target[j]==target[i]:
                j=j-1
            i=j
            count=count+1
        if target[0]=="0":
            return count-1
        else:
            return count
