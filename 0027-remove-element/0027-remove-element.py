class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        cnt=0
        j=0
        n=len(nums)
        for i in range(0,len(nums)):
            if nums[i]!=val:
                nums[j]=nums[i]
                j+=1
            else:
                cnt+=1
        return len(nums)-cnt
        

                
            
        return cnt
                