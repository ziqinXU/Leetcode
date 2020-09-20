class Solution:
    def reorderSpaces(self, text: str) -> str:
        spaces=text.count(" ")
        
        textlist=text.split(" ")
        
        returnstring=""
        i=0
        while i<len(textlist):
            
            if textlist[i]=='':
                del textlist[i]
                i=i-1
            i+=1
        if len(textlist)>1:
            group=spaces//(len(textlist)-1)
            rest=spaces%(len(textlist)-1)
            for i in range(len(textlist)-1):
                returnstring+=textlist[i]
                returnstring+=' '*group
            returnstring+=textlist[-1]
            returnstring+=' '*rest
            return returnstring
        else:
            returnstring+=textlist[0]
            returnstring+=spaces*' '
            return returnstring
