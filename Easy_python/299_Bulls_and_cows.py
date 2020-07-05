class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        secretdict=Counter(secret)
        guessdict=Counter(guess)
        count=0x
        for i in range(len(secret)):
            if secret[i]==guess[i]:
                count=count+1
        count2=0
        for i in secretdict:         
            if i in guessdict:            
                count2=count2+min(secretdict[i],guessdict[i])
        returnarray=str(count)+"A"+str(count2-count)+"B"
        return returnarray
