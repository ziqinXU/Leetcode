class Solution:
    def reformatDate(self, date: str) -> str:
        Month=["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        newstring=date.split()[::-1]
        return "%s-%02d-%02d" % (newstring[0], Month.index(newstring[1])+1, int(newstring[2][:-2]))
