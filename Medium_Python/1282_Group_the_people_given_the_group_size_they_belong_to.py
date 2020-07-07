class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        #对序号排序，看当前数，组的大小是多少
        sortedindex=sorted(range(len(groupSizes)),key=lambda k:groupSizes[k])
        returnlist=[]
        j=0
        while True:
            k=0
            templist=[]
            number=groupSizes[sortedindex[j]]
            while j<len(sortedindex) and k<number:
                templist.append(sortedindex[j])
                k=k+1
                j=j+1
            returnlist.append(templist)
            if j==len(sortedindex):
                break
        return returnlist

