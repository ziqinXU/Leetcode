#HASHMAP/dict 储存已经出现过的序列，超过一次则添加至returnlist，注意重复部分
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        dictDNA={}
        returnlist=[]
        for i in range(len(s)-10+1):
            if s[i:i+10] in dictDNA and dictDNA[s[i:i+10]]==1:
                returnlist.append(s[i:i+10])
                dictDNA[s[i:i+10]]+=1
            elif  s[i:i+10] not in dictDNA:
                dictDNA[s[i:i+10]]=1
            else:
                dictDNA[s[i:i+10]]+=1
        #print(dictDNA)
        return returnlist
            
