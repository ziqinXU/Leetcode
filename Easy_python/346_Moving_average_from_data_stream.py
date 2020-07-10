class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.size=size
        self.res=[]

    def next(self, val: int) -> float:
        size=self.size
        res=self.res
        res.append(val)
        if len(self.res)<=self.size:
            return sum(res)/len(res)
        else:
            del res[0]
            return sum(res)/size



# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
