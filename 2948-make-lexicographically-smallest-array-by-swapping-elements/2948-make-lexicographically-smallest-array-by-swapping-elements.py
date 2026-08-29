class Solution:
    def lexicographicallySmallestArray(self, nums: list[int], limit: int) -> list[int]:
        n = len(nums)
        
        # Pair each element with its original index so we don't lose track of positions
        indexed_nums = sorted((num, i) for i, num in enumerate(nums))
        
        res = [0] * n
        i = 0
        
        while i < n:
            # Find a group of numbers where consecutive elements differ by <= limit
            j = i
            while j + 1 < n and indexed_nums[j + 1][0] - indexed_nums[j][0] <= limit:
                j += 1
                
            # Extract the indices and values for the current group
            group = indexed_nums[i:j + 1]
            indices = sorted(item[1] for item in group)
            values = sorted(item[0] for item in group)
            
            # Place the sorted values back into their sorted original index positions
            for idx, val in zip(indices, values):
                res[idx] = val
                
            # Move to the next group
            i = j + 1
            
        return res