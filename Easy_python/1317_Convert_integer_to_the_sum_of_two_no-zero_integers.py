class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        number1=1
        number2=0
        while True:
            if str(number1).count('0')==0:
                number2=n-number1
                if str(number2).count('0')==0:
                    break
            number1=number1+1
        return [number1,number2]
