class Solution:
    def decodeString(self, s: str) -> str:
        """
        构建辅助栈 stack， 遍历字符串 s 中每个字符 c；
        -当 c 为数字时，将数字字符转化为数字 multi，用于后续倍数计算；
        -当 c 为字母时，在 res 尾部添加 c；
        -当 c 为 [ 时，将当前 multi 和 res 入栈，并分别置空置 
            记录此 [ 前的临时结果 res 至栈，用于发现对应 ] 后的拼接操作；
            记录此 [ 前的倍数 multi 至栈，用于发现对应 ] 后，获取 multi × [...] 字符串。
            进入到新 [ 后，res 和 multi 重新记录。
        -当 c 为 ] 时，stack 出栈，拼接字符串 res = last_res + cur_multi * res，其中:
        last_res是上个 [ 到当前 [ 的字符串，例如 "3[a2[c]]" 中的 a；
        cur_multi是当前 [ 到 ] 内字符串的重复倍数，例如 "3[a2[c]]" 中的 2。
        返回字符串 res。
        作者：jyd
        """
        stack=[]
        res=""
        multi=0
        for i in range(len(s)):
            if '0'<=s[i] and s[i]<='9':
                multi = multi * 10 + int(s[i])
            elif s[i]>='a' and s[i]<='z' or s[i]>='A' and s[i]<='Z':
                res+=s[i]
            elif s[i]=='[':
                stack.append([multi,res])
                multi=0
                res=""
            elif s[i]==']':
                res=stack[-1][1]+stack[-1][0]*res
                stack.pop()

        return res
