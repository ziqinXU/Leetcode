class Solution:
    def mostVisited(self, n: int, rounds: List[int]) -> List[int]:

    #如果开头小于结尾，那么中间这些数是最多的。
    #如果开头等于结尾，那么就开头（也即结尾）这一个数最多
    #如果开头大于结尾，那么从1到结尾，和从开头到n，最多。---思路来源于胖虎101

        if rounds[-1]>rounds[0]:
            return [x for idx,x in enumerate(range(rounds[0],rounds[-1]+1))]
        elif rounds[-1]==rounds[0]:
            return [rounds[0]]
        else:
            returnarr=[x for idx,x in enumerate(range(1,rounds[-1]+1))]+[x for idx,x in enumerate(range(rounds[0],n+1))]
            return returnarr
