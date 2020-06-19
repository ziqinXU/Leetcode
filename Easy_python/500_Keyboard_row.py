class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        A=['Q','W','E','R','T','Y','U','I','O','P','q','w','e','r','t','y','u','i','o','p'];
        B=['A','S','D','F','G','H','J','K','L','a','s','d','f','g','h','j','k','l'];
        C=['Z','X','C','V','B','N','M','z','x','c','v','b','n','m'];
        returnarray=[]
        for idx, word in enumerate(words):
            first=word[0]
            if first in A:
                count=0
            if first in B:
                count=1
            if first in C:
                count=2
            flag=0
            for i in range(1,len(word)):
                if word[i] in A:
                    count1=0
                if word[i] in B:
                    count1=1
                if word[i] in C:
                    count1=2
                if count1!=count:
                    flag=1
                    break
            if flag==0:
                returnarray.append(word)
        return returnarray

            
                
        
