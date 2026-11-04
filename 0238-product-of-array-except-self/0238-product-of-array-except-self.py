class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        total=1
        if 0 not in nums:
            total=1
            for j in nums:
                total*=j
            result = list(map(lambda x: int(total / x), nums))
            return result


        ans=[0]*len(nums)
        for i in range(0,len(nums)):
            total=1
            new_arr=nums[:i]+nums[i+1:]
            for j in new_arr:
                total*=j
            ans[i]=total
        return ans
        