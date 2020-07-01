class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        returnarray=[]
        sortedarray=sorted(arr)
      
        for i in range(len(arr)-1):
            if arr[i]<sortedarray[len(sortedarray)-1]:
                returnarray.append(sortedarray[len(sortedarray)-1])
                del sortedarray[sortedarray.index(arr[i])]
            else:
                del sortedarray[len(sortedarray)-1]
                returnarray.append(sortedarray[len(sortedarray)-1])
        returnarray.append(-1)
        return returnarray
            
