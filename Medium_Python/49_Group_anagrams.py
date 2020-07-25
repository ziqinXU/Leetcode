class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        pos = [0]*len(strs)
        dictstrs = {}
        returnlist=[]
        for i in range(len(strs)):
            temp = ''.join(sorted(strs[i]))
            if temp in dictstrs:
                dictstrs[temp].append(i) 
            else:
                dictstrs[temp] = [i]
        for words in dictstrs:
            tempstring = []
            j = 0
            while j < len(dictstrs[words]):
                tempstring.append(strs[dictstrs[words][j]])
                j = j + 1
            returnlist.append(tempstring)            
        return returnlist
