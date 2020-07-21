class Solution:
    def areSentencesSimilar(self, words1: List[str], words2: List[str], pairs: List[List[str]]) -> bool:
        if len(words1)!=len(words2):
            return False
        else:
            pairs_set = [set(pairs[i]) for i in range(len(pairs))]
            for i in range(len(words1)):
                templist=[]
                templist.append(words1[i])
                templist.append(words2[i])
                if words1[i]!=words2[i] and set(templist) not in pairs_set:
                    return False
            return True
