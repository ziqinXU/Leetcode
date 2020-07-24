class Logger:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.time=[]
        self.content=[]
        

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        """
        if message not in self.content:
            self.content.append(message)
            self.time.append(timestamp)
            return True
        elif timestamp-self.time[self.content.index(message)]>=10:
            del self.time[self.content.index(message)]
            del self.content[self.content.index(message)]
            self.content.append(message)
            self.time.append(timestamp)
            return True
        return False




# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)
