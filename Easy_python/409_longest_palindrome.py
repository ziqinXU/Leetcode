class Solution:
    def longestPalindrome(self, s: str) -> int:
        #偶数直接相加，奇数只用偶数次部分，总和中判断是否还剩一个单独字母可加
        A=Counter(s)
        length=0
        for i in A:
            if A[i]%2==0:
                length=length+A[i]
            else:
                length=length+A[i]-1
        if length==len(s):
            return length
        else:
            return length+1
