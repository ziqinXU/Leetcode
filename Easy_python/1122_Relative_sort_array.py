class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        returnarray=[]
        for i in range(len(arr2)):    
            j=0
            while j<len(arr1):
                if arr1[j]==arr2[i]:
                    returnarray.append(arr2[i])
                    del arr1[j]
                    j=j-1
                j=j+1
        arr1=sorted(arr1)
        for i in range(len(arr1)):
            returnarray.append(arr1[i])
        return returnarray
            
