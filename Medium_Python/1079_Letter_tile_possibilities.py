class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        #每从字典中提取一个字母，减少1，回溯后再加回
        totalcount=0
        dicttiles=Counter(tiles)
        def backtrack(dicttiles,totalcount):
            for alpha in dicttiles:
                if dicttiles[alpha]==0:#找下一个字母
                    continue
                else:
                    totalcount+=1
                    dicttiles[alpha]-=1
                    totalcount=backtrack(dicttiles,totalcount)
                    dicttiles[alpha]+=1
            return totalcount
        totalcount=backtrack(dicttiles,totalcount)
        return totalcount
