class Solution:
    def differByOne(self, dict: List[str]) -> bool:
        #将每一位替换成别的字符，看是否在set中已经存在该字符
        dictset=set()
        for i in range(len(dict)):
            for j in range(len(dict[i])):
                
                if dict[i][:j]+'*'+dict[i][j+1:] in dictset:
                    return True
                else:
                    dictset.add(dict[i][:j]+'*'+dict[i][j+1:])
        return False
