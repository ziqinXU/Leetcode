class Solution:
    def freqAlphabets(self, s: str) -> str:
        firstgroup=['1','2','3','4','5','6','7','8','9']
        secondgroup=['10#','11#','12#','13#','14#','15#','16#','17#','18#','19#','20#','21#','22#','23#','24#','25#','26#']
        for i in range(len(secondgroup)):
            s = s.replace("%d#" %(i+10), chr(i + 97+9))#should assign s to s
            #print(secondgroup[i], chr(i+ord('j')))
            #s = s.replace(secondgroup[i], chr(i+ord('j')))

        for j in range(len(firstgroup)):
            #s = s.replace(firstgroup[j], chr(j + 97))
            s = s.replace("%d" %(j+1), chr(j + 97))
            
        return s
