class Solution:
    def shortestDistance(self, words: List[str], word1: str, word2: str) -> int:
        arr1=[]
        arr2=[]
        for idx, word in enumerate(words):
            if word==word1:
                arr1.append(idx)
            if word==word2:
                arr2.append(idx)
        mindis=len(words)+1
        for i in range(len(arr1)):
            for j in range(len(arr2)):
                if abs(arr1[i]-arr2[j])<mindis:
                    mindis=abs(arr1[i]-arr2[j])
        return mindis

