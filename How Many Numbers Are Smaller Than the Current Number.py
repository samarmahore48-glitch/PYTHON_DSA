class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        count=[0]*len(nums)
        for i in range(0,len(nums)):
            for j in nums[::]:
                if nums[i]>j:
                    count[i]+=1
        return count