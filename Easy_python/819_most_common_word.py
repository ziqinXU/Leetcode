class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph=paragraph.lower()
        symbols=['!','?','\'',',',';','.']
        for i in range(len(symbols)):
            paragraph=paragraph.replace(symbols[i]," ")
        paragraph=paragraph.split()
        A=Counter(paragraph)
        paragraph=sorted(A,reverse=True,key=lambda k:A[k])
        for i in range(len(paragraph)):
            if paragraph[i] not in banned:
                return paragraph[i]
       
