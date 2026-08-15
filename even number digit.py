class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        
        countt=0
        for i in nums:
            count=0
            while i>0:
                count+=1
                i//=10
            if count%2==0:
                countt+=1
        return countt  

        