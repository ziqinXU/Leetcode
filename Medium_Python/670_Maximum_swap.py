class Solution:
    def maximumSwap(self, num: int) -> int:
        #如果数组非增，返回原数，否则找出升序后数组部分的最后一个最大数字与左边开始第一个比他小的数字交换
        arrlist=list(map(int,str(num)))
        pos=0
        flag=0
        for i in range(len(arrlist)-1):
            if arrlist[i+1]>arrlist[i]:
                pos=i
                flag=1
                break
        if flag==0:
            return num
        else:
            maxval=max(arrlist[pos:])
            maxindex=len(arrlist)-1-arrlist[::-1].index(max(arrlist[pos:]))
            for i in range(len(arrlist)):
                if arrlist[i]<maxval:
                    pos=i
                    break

            arrlist[maxindex]=arrlist[pos]
            arrlist[pos]=maxval
            return int(''.join(map(str,arrlist)))
