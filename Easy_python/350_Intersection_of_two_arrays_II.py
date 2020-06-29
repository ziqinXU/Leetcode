class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        returnlist=[]
        for i in range(len(nums1)):
            if nums1[i] in nums2:
                del nums2[nums2.index(nums1[i])]
                returnlist.append(nums1[i])
        return returnlist
