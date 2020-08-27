class StringIterator:

    def __init__(self, compressedString: str):
        self.string=[]
        i=0
        while i < len(compressedString):
            if compressedString[i].isalpha():
                self.string.append(compressedString[i])
                j=i+1
                while j< len(compressedString) and compressedString[j].isdigit():
                    j=j+1
                #print(i,j)
                #print(compressedString[i:j])
                self.string.append(int(compressedString[i+1:j]))
                i=j-1
            i=i+1
            
                

    def next(self) -> str:
        #print(self.string)
        if len(self.string)==0:
            return ' '
        if int(self.string[1])==1:
            a=self.string[0]
            del self.string[0]
            del self.string[0]
            return a
        if int(self.string[1])>1:
            self.string[1]=str(int(self.string[1])-1)
            return self.string[0]
            
    def hasNext(self) -> bool:
        if len(self.string)==0:
            return False
        else:
            return True



# Your StringIterator object will be instantiated and called as such:
# obj = StringIterator(compressedString)
# param_1 = obj.next()
# param_2 = obj.hasNext()
