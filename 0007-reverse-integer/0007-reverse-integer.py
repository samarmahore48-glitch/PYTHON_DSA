class Solution:
    def reverse(self, x: int) -> int:
        n=abs(x)
        last = n%10
        n//=10
        final = last
        while n>0:
            last = n%10
            n//=10
            final = final *10+ last 
        if final <= -2**31 or final >= (2**31)-1:
            return 0
        if x >0:
            return final
        else :
            return -1*final


        