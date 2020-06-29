class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        returnlist=[]
        indexsum=[]
        for i in range(len(list1)):
            if list1[i] in list2:
                returnlist.append(list1[i])
                indexsum.append(list2.index(list1[i])+i)
        j=0
        while j < len(returnlist):
            if indexsum[j]!=min(indexsum):
                del returnlist[j]
                j=j-1
            j=j+1
        return returnlist
