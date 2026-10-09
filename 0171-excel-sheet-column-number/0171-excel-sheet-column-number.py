class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        res=0
        for i in columnTitle:
            val=ord(i)-64
            res=res*26 + val
        return res

        