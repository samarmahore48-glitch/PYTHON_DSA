class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        fac=[]
        for i in range (1,int((n**0.5)+1)):
            if n%i==0:
                fac.append(i)
                if i!=n//i:
                    fac.append(n//i)
        fac.sort()
        if len(fac)>=k:
            return fac[k-1]
        return -1
    

        






        return -1