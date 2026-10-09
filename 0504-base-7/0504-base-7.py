class Solution:
    def convertToBase7(self, num: int) -> str:
        if num==0:
            return "0"
        ans=''
        n=abs(num)
        while n>0:
            las=n%7
            n//=7
            ans+=str(las)
        if num<0:
            return "-"+ans[::-1]
        return ans [::-1]