class ProductOfNumbers:
    #前缀积，注意0时清空列表，如果此时k大于前缀积数组长度，则说明之前有0
    def __init__(self):
        self.arr=[]
        self.pre=[1]
        
    def add(self, num: int) -> None:
        self.arr.append(num)
        if num==0:
            self.pre=[1]
        else:
            self.pre.append(self.pre[-1]*num)
    def getProduct(self, k: int) -> int:
        if k>=len(self.pre):
            return 0
        else:
            return self.pre[-1]//self.pre[-1-k]


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)
