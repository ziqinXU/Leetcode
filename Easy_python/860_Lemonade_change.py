class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        dictstart={5:0,10:0,20:0}
        for i in range(len(bills)):
            if bills[i]==5:
                dictstart[5]=dictstart[5]+1
            elif bills[i]==10:
                dictstart[10]=dictstart[10]+1
                if dictstart[5]>=1:
                    dictstart[5]=dictstart[5]-1
                else:
                    return False
            else:
                dictstart[20]=dictstart[20]+1
                if dictstart[10]>=1:
                    dictstart[10]=dictstart[10]-1
                    if dictstart[5]>=1:
                        dictstart[5]=dictstart[5]-1
                    else:
                        return False
                else:
                    if dictstart[5]>=3:
                        dictstart[5]=dictstart[5]-3
                    else:
                        return False
        return True
