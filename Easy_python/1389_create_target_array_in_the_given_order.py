class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        returnlist=[]
        for idx in range(len(index)):
            returnlist.insert(index[idx],nums[idx])
        return returnlist
