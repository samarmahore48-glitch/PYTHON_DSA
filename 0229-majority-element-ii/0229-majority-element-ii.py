class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        # Calculate the required threshold
        threshold = len(nums) // 3
        
        # Count frequencies of each number
        freq = {}
        for i in nums:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1  # Fix 1: Initialize count to 1, not 0
        
        # Fix 2: Collect all elements that exceed the threshold
        result = []
        for key, count in freq.items():
            if count > threshold:
                result.append(key)
                
        return result
