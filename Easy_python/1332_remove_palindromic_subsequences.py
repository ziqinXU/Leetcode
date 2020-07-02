class Solution:
    def removePalindromeSub(self, s: str) -> int:
        #删除子序列：可一次删除所有a，一次所有b
        if len(s)==0:
            return 0
        else:
            flag=0
            for i in range(int(len(s)/2)):
                if s[i]!=s[len(s)-i-1]:
                    flag=1
                    break
            if flag==1:
                return 2
            else:
                return 1
