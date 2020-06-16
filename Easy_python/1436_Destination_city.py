class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        current = paths[0][1]
        i=0
        while i < len(paths):
            if paths[i][0]==current:
                current=paths[i][1]
                i=0      
            i=i+1
        return current
