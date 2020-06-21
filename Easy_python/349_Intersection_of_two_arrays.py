class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dict1={}
        dict2={}
        returnarray=[]
        for idx,number1 in enumerate(nums1):
            dict1[number1]=nums1.count(number1)
        for idx,number2 in enumerate(nums2):
            dict2[number2]=nums2.count(number2)
        for i in dict1:
            if i in dict2:
                returnarray.append(i)
        return returnarray

        
