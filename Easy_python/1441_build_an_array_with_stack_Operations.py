class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:

        returnlist=[]
        for i in range(1,target[len(target)-1]+1):
            if i not in target:
                returnlist.append("Push")
                returnlist.append("Pop")
            else:
                returnlist.append("Push")
        return returnlist
