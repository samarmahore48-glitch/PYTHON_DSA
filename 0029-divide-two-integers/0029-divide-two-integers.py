class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        if dividend == INT_MIN and divisor == -1:
            return INT_MAX
        count=0
        ans=0
        sign=''
        if (dividend > 0 and divisor <0) or  (dividend < 0 and divisor > 0) :
            sign = 'neg'
        n =abs(dividend)
        d=abs(divisor)
        temp=d
        while n>=d:
            count=0
            while n>= (d<<count+1):
                count+=1
            ans+=(1<<count)
            n-= d<< count
            


        if sign=='neg':
            return -ans
        return ans