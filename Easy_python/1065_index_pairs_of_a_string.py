class Solution:
    def indexPairs(self, text: str, words: List[str]) -> List[List[int]]:
        temppos=[]
        returnarray=[]
        for idx,word in enumerate(words):
            k=0
            k1=0
            while text.find(word,k)!=-1:
                k1=text.find(word,k)
                k=k1+1
                temppos=[k1,k1+len(word)-1]
                returnarray.append(temppos)
        returnarray=sorted(returnarray)
        return returnarray
