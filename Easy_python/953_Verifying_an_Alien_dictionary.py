class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        for i in range(len(words)-1):
            firstword=words[i]
            nextword=words[i+1]
            flag=0
            for j in range(min(len(firstword),len(nextword))):
                if firstword[j]!=nextword[j]:
                    flag=1
                    if order.find(firstword[j])>order.find(nextword[j]):
                        return False
                    elif order.find(firstword[j])<order.find(nextword[j]):
                        break
           
            if flag==0:
                if len(firstword)>len(nextword):
                    return False
        return True

