class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        output=[0]*len(nums)
        j=0
        for i in nums:
            output[j]=nums[i]
            j+=1
        return output
        