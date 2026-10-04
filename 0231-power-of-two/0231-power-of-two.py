class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        
        if n%2!=0 and n>1:
            return False
        
        if n>=0:
            for i in range (0,int(n**0.5)+2):
                if 2**i==n:
                    return True
            return False
        return False