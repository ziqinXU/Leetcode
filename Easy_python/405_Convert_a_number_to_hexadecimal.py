class Solution:
    def toHex(self, num: int) -> str:
        res=[]
        if num < 0:
            num = (abs(num) ^ ((2 ** 32) - 1)) + 1
        while(int(num/16)!=0):
            if num%16<=9:
                res.append(str(num%16))
            else:
                res.append(chr(num%16-10+ord('a')))
            num=int(num/16)
        if num%16<=9:
            res.append(str(num%16))
        else:
            res.append(chr(num%16-10+ord('a')))
        res.reverse()
        return ''.join(res)
        
