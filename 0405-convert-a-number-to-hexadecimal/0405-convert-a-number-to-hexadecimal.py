class Solution:
    def toHex(self, num: int) -> str:
        if num==0:
            return "0"
        if num<0:
            num= 4294967296 + num
        val='0123456789abcdef'
        res=''
        while num > 0:
            res+=val[num%16]
            num//=16
        return res[::-1]


        