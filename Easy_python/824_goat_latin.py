class Solution:
    def toGoatLatin(self, S: str) -> str:
        newlist=list(S.split())
        vowel=['a','e','i','o','u','A','E','I','O','U']
        for i in range(len(newlist)):
            if newlist[i][0] in vowel:
                newlist[i]=newlist[i]+"ma"
            else:
                templist=newlist[i][1:]
                templist=templist+newlist[i][0]
                newlist[i]=templist+"ma"
            newlist[i]=newlist[i]+"a"*(i+1)
        return " ".join(newlist)
