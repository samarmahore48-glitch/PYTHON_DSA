class Solution:
    def countDigits(self, num: int) -> int:
        count=0
        all_num=[]
        n=num
        while n>0:
            all_num.append(n%10)
            n//=10
        for i in all_num:
            if num%i==0:
                count+=1
        return count
            
        