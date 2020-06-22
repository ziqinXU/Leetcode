class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        returnlist=[]
        for i in range(1,n+1):
            if i%3==0 and i%5==0:
                returnlist.append("FizzBuzz")
            elif i%3==0:
                returnlist.append("Fizz")
            elif i%5==0:
                returnlist.append("Buzz")
            else:
                returnlist.append(str(i))
        return returnlist
