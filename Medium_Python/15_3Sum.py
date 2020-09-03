class Solution:
    #先排序，然后遍历，left=i+1,right=len(nums)-1,若小于0，则加上left，若大于，则减去
    #如果当前值大于0，结束循环，如果当前下一个相等，跳过，如果sum=0时，左边+1相等，跳过，同理右边-1
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums)<3:
            return [];
        left=1
        right=len(nums)-1
        nums=sorted(nums)
        i=0
        returnarr=[]
        while i<len(nums)-2:
            if nums[i]>0:
                break
            while left<right:
                if nums[i]+nums[left]+nums[right]<0:
                    left=left+1
                elif nums[i]+nums[left]+nums[right]>0:
                    right=right-1
                else:
                    #if [nums[i],nums[left],nums[right]] not in returnarr:
                    returnarr.append([nums[i],nums[left],nums[right]])
                    while left< right and left+1<len(nums) and nums[left+1]==nums[left]:
                        left=left+1
                    while left<right and nums[right-1]==nums[right]:
                        right=right-1
                    left=left+1
            while i+1<len(nums) and nums[i+1]==nums[i]:
                i=i+1
            i=i+1
            left=i+1
            right=len(nums)-1
            
        return returnarr
