class Solution:
    def myPow(self, x: float, n: int) -> float:
        ans=1.0
        
        if n==0:
            return 1.0
        abs_n=abs(n)

        while abs_n >0:
            if abs_n % 2 == 1:
                ans *=x
            x*=x
            abs_n//=2
        return ans if n>0 else 1/ans




        