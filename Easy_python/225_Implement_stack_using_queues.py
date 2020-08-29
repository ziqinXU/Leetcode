class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue=[]


    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.queue.append(x)



    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """

        top=self.queue[-1]
        del self.queue[-1]
        return top


    def top(self) -> int:
        """
        Get the top element.
        """
        top=self.queue[-1]
        return top



    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        if len(self.queue)==0:
            return True
        else:
            return False



# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
