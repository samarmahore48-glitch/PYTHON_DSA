class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        result=[0]*len(nums)
        l=1
        s=0
        for i in range (len(nums)):
            if nums[i]%2==0:
                result[s]=nums[i]
                s+=2
            else:
                result[l]=nums[i]
                l+=2
        return result


        