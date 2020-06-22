class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        result=[]
        resultstring=""
        for i in range(len(emails)):
            k=emails[i].find("@")
            tempstring=emails[i][:k]
            tempstring=tempstring.replace(".", "")
            if tempstring.find("+")!=-1:
                j=tempstring.find("+")
                tempstring=tempstring[0:j]
            resultstring=tempstring+emails[i][k:]
            result.append(resultstring)
        return len(list(set(result)))

                
                    



