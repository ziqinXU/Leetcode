class Solution:
    def findLonelyPixel(self, picture: List[List[str]]) -> int:
        count=0
        for i in range(len(picture)):
            if 'B' in picture[i] and picture[i].count('B')==1:
                j=picture[i].index('B')
                flag=0
                for k in range(len(picture)):
                    if picture[k][j]=='B' and k!=i:
                        flag=1
                        break
                print(j,i)
                if flag==0:
                    count=count+1
        return count
