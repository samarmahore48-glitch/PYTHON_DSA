class Solution:
    def nthUglyNumber(self, n: int) -> int:
        if n<7:
            return n
        arr= [0]*n
        arr[0]=1
        p1,p2,p3=0,0,0
        for  i in range(1,n):
            dig=min(2*arr[p1],3*arr[p2],5*arr[p3])
            arr[i]=dig
            if dig==2*arr[p1]:
                p1+=1
            if dig==3*arr[p2]:
                p2+=1
            if dig==5*arr[p3]:
                p3+=1
        return arr[-1]
                

        