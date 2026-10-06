class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if a=="0" and b=="0":
            return "0"
        max_len=max(len(a),len(b))
        a = a.zfill(max_len)
        b = b.zfill(max_len)
        res=[0]*(max_len+1)
        carry=0
        for i in range(max_len-1,-1,-1):
            total=int(a[i])+int(b[i])+carry
            carry=total//2
            if total%2!=0:
                res[i+1]=1
        if carry==1:
            res[0]="1"
        else:
            res=res[1:]
        ans=''
        for i in res:
            ans+=str(i)
        return ans

                
        

