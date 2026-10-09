class Solution:
    def arrangeCoins(self, n: int) -> int:
        res=0
        while n > res:
            res+=1
            n-=res
        return res



        