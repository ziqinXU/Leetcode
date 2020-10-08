class Solution:
    def filterRestaurants(self, restaurants: List[List[int]], veganFriendly: int, maxPrice: int, maxDistance: int) -> List[int]:
        res=[]
        for i in range(len(restaurants)):
            if veganFriendly==1:
                if restaurants[i][2]==veganFriendly and restaurants[i][3]<=maxPrice and restaurants[i][4]<=maxDistance:
                    res.append([restaurants[i][0],restaurants[i][1]])
            else:
                if restaurants[i][3]<=maxPrice and restaurants[i][4]<=maxDistance:
                    res.append([restaurants[i][0],restaurants[i][1]])
        
        finalresult = sorted(res, key=lambda restaurants: (-restaurants[1],-restaurants[0]))
        return [i[0] for i in finalresult]
