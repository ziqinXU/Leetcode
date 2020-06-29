class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        count=Counter(text)
        numberlist=[]
        numberlist.append(count['a'])
        numberlist.append(count['b'])
        numberlist.append(count['n'])
        numberlist.append(int(count['l']/2))
        numberlist.append(int(count['o']/2))
        return min(numberlist)
