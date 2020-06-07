class Solution:
    def sumOfDigits(self, A: List[int]) -> int:
        minnumber=sys.maxsize
        for number in A:
            if number<minnumber:
                minnumber=number
        sumelement=0
        while(minnumber%10!=0):
            sumelement=sumelement+minnumber%10
            minnumber=int(minnumber/10);
        if sumelement%2==1:
            return 0
        else:
            return 1
        
