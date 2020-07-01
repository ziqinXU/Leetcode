class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        licensePlate=licensePlate.lower()
        licencedict=Counter(licensePlate)
        returnword=[]
        newlicencedict={}
        for i in licencedict:
            if i<="z" and i>="a":
                newlicencedict[i]=licencedict[i]
        currentlen=20
        for j in range(len(words)):
            flag=0
            temp=Counter(words[j])
            for i in newlicencedict:
                if i in temp and newlicencedict[i]<=temp[i]:
                    flag=0
                else:
                    flag=1
                    break
            if flag==0:
                if len(words[j])<currentlen:
                    currentlen=len(words[j])
                    returnword=words[j]
            temp={}
        return returnword

        
