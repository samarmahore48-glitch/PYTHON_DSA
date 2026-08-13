class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        v1=v2=v3=float('-inf')
        for i in nums:
            if i in (v1,v2,v3):
                continue
            if i>v1:
                v3=v2
                v2=v1
                v1=i
                
            elif i>v2:
                v3=v2
                v2=i
            elif i>v3:
                v3=i
        return v3 if v3!=float('-inf') else v1
