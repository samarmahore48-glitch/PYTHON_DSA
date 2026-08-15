class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        summ=[0]*len(nums)
        summ[0]=nums[0]
        for i in range (1,len(nums)):
            summ[i]=summ[i-1]+nums[i]
        return summ
        