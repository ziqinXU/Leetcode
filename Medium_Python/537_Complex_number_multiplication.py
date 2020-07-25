class Solution:
    def complexNumberMultiply(self, a: str, b: str) -> str:
        alist = a.split('+')
        blist = b.split('+')
        a1 = int(alist[0])
        a2 = int(alist[1][:-1])
        b1 = int(blist[0])
        b2 = int(blist[1][:-1])
        returnstring = ""
        returnstring = returnstring + str(a1*b1+a2*b2*(-1)) + "+"
        returnstring = returnstring + str(a1*b2+a2*b1) + "i"
        return returnstring
