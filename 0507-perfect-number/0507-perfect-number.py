class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num<= 1:
            return False
        lis=[]
        for i in range (1,int((num**0.5)+1)):
            if num%i==0:
                lis.append(i)
                if i!=num//i:
                    lis.append(num//i)
        return (sum(lis)-num)==num