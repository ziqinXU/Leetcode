class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        returnarray=[]
        for i in range(len(nums1)):
            flag=0
            start=nums2.index(nums1[i])
            for j in range(start+1,len(nums2)):
                if nums2[j]>nums1[i]:
                    returnarray.append(nums2[j])
                    flag=1
                    break
            if flag==0:
                returnarray.append(-1)
        return returnarray
