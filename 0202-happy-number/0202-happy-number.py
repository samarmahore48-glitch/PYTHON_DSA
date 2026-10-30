class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        
        while n != 1 and n not in seen:
            seen.add(n)
            
            # Sum the squares of the digits of n
            val = 0
            temp = n
            while temp > 0:
                last = temp % 10
                val += last ** 2
                temp //= 10
            
            n = val
            
        return n == 1