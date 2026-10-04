class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n==1:
            return True 
        if n<4 :
            return False
        for i in range (1,int(n**(1/4)+2)):
            if 4**i==n:
                return True
        return False
        
        
        
        