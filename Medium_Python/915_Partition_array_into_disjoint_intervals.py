class Solution:
    def partitionDisjoint(self, A: List[int]) -> int:
        #找出左边最大，右边最小，保证左边最大小于右边最小
        maxleft,minright=[0],[1000000]
        for i in range(len(A)):
            maxleft.append(max(maxleft[-1],A[i]))
        del maxleft[0]
        for i in reversed(range(0,len(A))):
            minright.append(min(minright[-1],A[i]))
        del minright[0]
        minright=minright[::-1]
        #print(maxleft,minright)
        for i in range(1,len(A)):
            if maxleft[i-1]<=minright[i]:
                return i
        
        
