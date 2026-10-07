class Solution:
    def trailingZeroes(self, n: int) -> int:
        x=1
        count=0
        while n>=5:
            count+=n//5
            n//=5
        return count
