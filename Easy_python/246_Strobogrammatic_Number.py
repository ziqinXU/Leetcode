class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        notstrob=['2','3','4','5','7']
        #changestrob=['6','9']
        strob=['0','8']
        for i in range(len(num)):
            if num[i] in notstrob:
                return False
            if num[i]=='6':
                if num[len(num)-1-i]!='9':
                    return False
            if num[i]=='9':
                if num[len(num)-1-i]!='6':
                    return False
            if num[i] in strob:
                if num[len(num)-1-i]!=num[i]:
                    return False
        return True
