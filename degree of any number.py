class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        freq = {}
        max_freq = 0
        for i in nums:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1
            if freq[i] > max_freq:
                max_freq = freq[i]                
        max_freq_elements = [num for num, count in freq.items() if count == max_freq]        
        min_length = len(nums)  
        for max_freq_element in max_freq_elements:
            start = 0
            last = 0
            for i in range(0, len(nums)):
                if nums[i] == max_freq_element:
                    start = i
                    break
            for i in range(len(nums)-1, -1, -1):
                if nums[i] == max_freq_element:
                    last = i + 1  # Kept your original i + 1 logic
                    break
            current_length = last - start
            if current_length < min_length:
                min_length = current_length
                
        return min_length
        