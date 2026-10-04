class Solution:
    def addDigits(self, num: int) -> int:
        if num<10:
            return num
        while num >= 10:
            ans = 0
            while num>0:
                last=num%10
                num//=10
                ans+=last
            if ans < 10:
                return ans
            else: 
                num= ans 

        
        