class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        A=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        returnarray=[]
        temparray = ""
        for idx,word in enumerate(words):
            for i in range(len(words[idx])):
                temparray=temparray+A[ord(words[idx][i])-ord('a')]
            if not temparray in returnarray:
                returnarray.append(temparray)
            temparray = ""
        return len(returnarray)
