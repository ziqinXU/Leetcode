class Solution:
    #双指针，从两头起，移动较小的一边（能保证之后的一定有机会比移动另一边大）
    def maxArea(self, height: List[int]) -> int:
        left,right=0,len(height)-1
        maxval=0
        while left<right:
            if min(height[left],height[right])*(right-left)>maxval:
                maxval=min(height[left],height[right])*(right-left)
            if height[left]>height[right]:
                right-=1
            else:
                left+=1
        return maxval
