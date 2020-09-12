class Solution:
    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        res=[]
        for i in range(len(favoriteCompanies)):
            found=0
            for j in range(len(favoriteCompanies)):
                if i!=j:
                    if len(list(set(favoriteCompanies[i]) & set(favoriteCompanies[j])))==len(favoriteCompanies[i]):
                        
                        
                        found=1
                        break
            
            if found==0:
                res.append(i)
        return res
