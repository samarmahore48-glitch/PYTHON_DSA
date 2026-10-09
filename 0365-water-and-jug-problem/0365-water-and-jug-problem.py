class Solution:
    def canMeasureWater(self, x: int, y: int, target: int) -> bool:
        a,b=x,y
        if target>x+y:
            return False
        if x+y==target or (x+y)/2==target:
            return True
        while b!=0:
            a,b=b,a%b
        gcd=a
        if target%gcd==0:
            return True
        return False



        