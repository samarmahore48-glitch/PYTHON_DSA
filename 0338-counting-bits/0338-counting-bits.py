class Solution:
    def countBits(self, n: int) -> list[int]:
        ans=[0]
        for i in range(1,n+1):
            count=0
            while i !=0 :
                count+=1
                i=i&(i-1)
            ans.append(count)
        return ans