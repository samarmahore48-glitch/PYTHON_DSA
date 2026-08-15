from typing import List

class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * n
        l_s = [0] * n
        r_s = [0] * n
        
        # Calculate left sums: start from index 1
        for i in range(1, n):
            l_s[i] = l_s[i - 1] + nums[i - 1]
            
        # Calculate right sums: start from index n-2 moving backward
        for i in range(n - 2, -1, -1):
            r_s[i] = r_s[i + 1] + nums[i + 1]
            
        # Calculate absolute difference
        for i in range(n):
            result[i] = abs(l_s[i] - r_s[i])
            
        return result
