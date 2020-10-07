class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        strdict={}
        for i in s:
            if i not in strdict:
                strdict[i]=1
            else:
                strdict[i]+=1
        count=0
        #最多能组成len(s)个，最少能组成奇数字母的个数（偶数组合到奇数内），当奇数个数为0时，能至少组成1组（偶数组）
        maxgroup=len(s)
        for i in strdict:
            if strdict[i]%2==1:
                count+=1
        if count==0:
            mingroup=1
        else:
            mingroup=count
        if mingroup<=k and k<=maxgroup:
            return True
        else:
            return False
