class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        res=[0]*(len(num1)+len(num2))
        num3= num1[::-1]
        num4= num2[::-1]
        ans=''
        for i in range(len(num3)):
            for j  in range(len(num4)):
                dig1=ord(num3[i])-ord('0')
                dig2=ord(num4[j])-ord('0')
                mul=dig1*dig2+res[i+j]
                res[i+j]=mul%10
                res[i+j+1]+=mul//10
        while len(res)>1 and res[-1]==0:
            res.pop()
        for  i in res:
            ans= ans+str(i)
        return ans[::-1]
                    