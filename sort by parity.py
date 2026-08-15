class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        result=[0]*len(nums)
        k=0
        l=len(nums)-1
        for i in range (len(nums)):
            if nums[i]%2==0:
                result[k]=nums[i]
                k+=1
            else:
                result[l]=nums[i]
                l-=1
        return result
        