class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        countlist=[]
        i=0
        while i< len(abbr):
            if abbr[i]<='z' and abbr[i]>='a':
                countlist.append(abbr[i])
                i=i+1
            else:
                temp=""
                while i<len(abbr) and (abbr[i]>='0' and abbr[i]<='9'):
                    temp=temp+abbr[i]
                    i=i+1
                    if temp[0]=='0':
                        return False
                countlist.append(temp)
        currentpos=0
        flag=0
        for i in range(len(countlist)):
            if currentpos>=len(word):
                flag=1
                break
            if len(countlist[i])>1 or (countlist[i]>"z" or countlist[i]<"a"):
                currentpos=currentpos+int(countlist[i])
            else:
                if word[currentpos]!=countlist[i]:
                    return False
                else:
                    currentpos=currentpos+1
            
        if currentpos!=len(word) or flag==1:
            return False   
        else:
            return True
