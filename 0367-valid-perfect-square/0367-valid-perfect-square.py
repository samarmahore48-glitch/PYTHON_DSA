class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l,h=0,num
        ans=False
        while l<=h:
            mid=(h+l)//2
            if mid*mid==num:
                return True
            if mid*mid>num:
                h=mid-1
            else:
                l=mid+1
        return False


            
