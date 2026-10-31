class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        if a==1 and b==1:
            return a

        lis1=[]
        count=0
        for i in range(1,int((a//2)+1)):
            if a%i==0:
                lis1.append(i)
        lis1.append(a)
        for i in range(1,int((b//2)+1)):
            if b%i==0:
                if i in lis1:
                    count+=1
        if b in lis1:
            count+=1
        return count
        