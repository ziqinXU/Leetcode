class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        dictpieces={}
        for i in range(len(pieces)):
            dictpieces[pieces[i][0]]=i#将piece中每组第一个数字作为key，组号为value
        t=0
        while t<len(arr):
            if arr[t] in dictpieces:
                cur=dictpieces[arr[t]]
                piecelen=len(pieces[cur])-1
                
                t+=1
                p=0
                
                while t<len(arr) and piecelen>0:
                    p+=1    

                    if arr[t]!=pieces[cur][p]:
                        return False
                    piecelen-=1
                    t+=1
            else:
                return False
        return True
            
