class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        else:
            if target<nums[0]:
                return 0
            elif target>nums[len(nums)-1]:
                return len(nums)
            else:
                for i in range(len(nums)):
                    if target>nums[i] and target<nums[i+1]:
                        return i+1
