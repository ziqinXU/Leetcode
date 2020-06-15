class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        returnarray=[]
        for i in range(int(len(nums)/2)):
            returnarray.append(nums[i])
            returnarray.append(nums[i+n])
        return returnarray
