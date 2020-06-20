class Solution:
    def findLucky(self, arr: List[int]) -> int:
        newlist=sorted(arr)
        diction={}
        for idx, number in enumerate(newlist):
            diction[number]=newlist.count(number)
        maxnumber=-1
        for i in diction:
            if diction[i]==i:
                maxnumber=i
        return maxnumber
            
