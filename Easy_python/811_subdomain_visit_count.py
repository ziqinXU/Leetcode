class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        numbers=[]
        domains=[]
        cpdomainsdict={}
        for i in range(len(cpdomains)):
            templist=cpdomains[i].split()
            numbers.append(int(templist[0]))
            domains.append(templist[1])
        for i in range(len(domains)):
            dotnumber=domains[i].count('.')
            if dotnumber==1:
                if domains[i] not in cpdomainsdict:
                    cpdomainsdict[domains[i]]=numbers[i]
                else:
                    cpdomainsdict[domains[i]]=cpdomainsdict[domains[i]]+numbers[i]
                index=domains[i].index('.')
                if domains[i][index+1:] not in cpdomainsdict:
                    cpdomainsdict[domains[i][index+1:]]=numbers[i]
                else:
                    cpdomainsdict[domains[i][index+1:]]=cpdomainsdict[domains[i][index+1:]]+numbers[i]
            else:
                if domains[i] not in cpdomainsdict:
                    cpdomainsdict[domains[i]]=numbers[i]
                else:
                    cpdomainsdict[domains[i]]=cpdomainsdict[domains[i]]+numbers[i]
                domainlist=domains[i].split('.')
                temp1='.'.join(domainlist[1:])
                if temp1 not in cpdomainsdict:
                    cpdomainsdict[temp1]=numbers[i]
                else:
                    cpdomainsdict[temp1]=cpdomainsdict[temp1]+numbers[i]
                temp2=domainlist[2]
                if temp2 not in cpdomainsdict:
                    cpdomainsdict[temp2]=numbers[i]
                else:
                    cpdomainsdict[temp2]=cpdomainsdict[temp2]+numbers[i]
        returnlist=[]
        for domains in cpdomainsdict:
            tempstring=""
            tempstring=str(cpdomainsdict[domains])+' '+domains
            returnlist.append(tempstring)
        return returnlist
