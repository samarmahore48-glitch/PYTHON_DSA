class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        low, i = 0, 0
        high = len(nums) - 1
        
        while i <= high:
            if nums[i] == 0:
                nums[low], nums[i] = nums[i], nums[low]
                low += 1
                i += 1  # We can safely move i forward because nums[low] was either 0 or 1
            elif nums[i] == 2:
                nums[high], nums[i] = nums[i], nums[high]
                high -= 1
                # Do NOT increment i here; we need to evaluate the new nums[i] next loop
            else:
                i += 1  # It's a 1, just leave it in place and move forward
