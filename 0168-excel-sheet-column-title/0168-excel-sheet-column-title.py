class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res=""
        while columnNumber>0:
        
            columnNumber-=1
            i=columnNumber%26
            j=chr(65+i)
            res+=j
            columnNumber//=26
        return res[::-1]




        