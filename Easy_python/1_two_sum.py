class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        newnums=sorted(nums)
        left=0
        right=len(nums)-1
        A=sorted(range(len(nums)), key=lambda k: nums[k])
        while left<right:
            if target==newnums[left]+newnums[right]:
                return [A[left],A[right]]
            elif target>newnums[left]+newnums[right]:
                left=left+1
            else:
                right=right-1
           
