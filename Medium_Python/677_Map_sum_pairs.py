class MapSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.mapdict={}

    def insert(self, key: str, val: int) -> None:
        if key not in self.mapdict:
            self.mapdict[key]=val
        else:
            self.mapdict[key]=val

    def sum(self, prefix: str) -> int:
        res=0
        for key in self.mapdict:
            if key.find(prefix)==0:
                res+=self.mapdict[key]
        return res


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)
