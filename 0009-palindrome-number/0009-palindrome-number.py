class Solution:
    def isPalindrome(self, x: int) -> bool:
        n=x
        last= n%10
        n//=10
        final = last
        while n>0:
            last=n%10
            n//=10
            final=final*10+last
        return final==x
            

        