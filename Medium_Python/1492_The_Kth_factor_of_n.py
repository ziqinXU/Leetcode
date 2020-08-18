class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        factorlist=[]
        
        factorlist.append(1)
        for i in range(2,int(math.sqrt(n))+1):
            if n%i==0:
                factorlist.append(i)
                if n//i!=i:
                    factorlist.append(n//i)
        if n!=1:
            factorlist.append(n)
        factorlist=sorted(factorlist)
        #print(factorlist)
        if k>len(factorlist):
            return -1
        else:
            return factorlist[k-1]
