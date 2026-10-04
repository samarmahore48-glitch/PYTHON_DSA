class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n==1:
            return True 
        if n<3 :
            return False
        for i in range (1,int(n**(1/3)+2)):
            if 3**i==n:
                return True
        return False
        
        
        