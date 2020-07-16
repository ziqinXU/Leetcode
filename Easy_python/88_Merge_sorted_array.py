class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i=len(nums1)-1
        while i>=0 and nums1[i]==0:
            i=i-1
        length=i+len(nums2)
        newnum=sorted(nums1[:i+1]+nums2)
        nums1[:length+1]=newnum[:]
