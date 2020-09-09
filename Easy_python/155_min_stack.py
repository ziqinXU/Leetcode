#用辅助栈记录最小值
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack=[]
        #self.minval=math.inf
        self.min_stack=[math.inf]
        

    def push(self, x: int) -> None:
        self.stack.append(x)
        if x>self.min_stack[-1]:
            self.min_stack.append(self.min_stack[-1])
        else:
            self.min_stack.append(x)
        

    def pop(self) -> None:
        del self.stack[-1]
        del self.min_stack[-1]

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
