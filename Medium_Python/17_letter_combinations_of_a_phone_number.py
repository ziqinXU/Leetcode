class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        bookdict={'2':['a','b','c'],'3':['d','e','f'],'4':['g','h','i'],'5':['j','k','l'],'6':['m','n','o'],'7':['p','q','r','s'],'8':['t','u','v'],'9':['w','x','y','z']}
        returnarr=[]
        if len(digits)==0:
            return []
        def dfs(index,templist):
            if index == len(digits):#当index等于电话号码位数时，加入
                returnarr.append("".join(templist))
            else:
                digit = digits[index]
                for alphabet in bookdict[digit]:
                    templist.append(alphabet)
                    dfs(index + 1,templist)
                    templist.pop()
        dfs(0,[])
        return returnarr
