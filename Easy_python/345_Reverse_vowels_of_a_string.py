class Solution:
    def reverseVowels(self, s: str) -> str:
        pos=[]
        vowellist=[]
        vowel="aeiouAEIOU"
        for i in range(len(s)):
            if s[i] in vowel:
                pos.append(i)
                vowellist.append(s[i])
        newlist=list(s)
        vowellist.reverse()
        for i in range(len(pos)):
            newlist[pos[i]]=vowellist[i]
        
        return ''.join(newlist)



