class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        nums.sort()
        sum=nums[-1]
        ans=sum
        while k!=1:
            ans+=(sum+1)
            sum+=1
            k-=1
        return ans
        