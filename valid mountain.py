class Solution:
    def validMountainArray(self, arr: list[int]) -> bool:
        # Check minimum length condition
        if len(arr) < 3:
            return False
            
        maxi = max(arr)
        peak_idx = arr.index(maxi)
        
        # Peak cannot be at the very start or the very end
        if peak_idx == 0 or peak_idx == len(arr) - 1:
            return False
            
        # 1. Check Uphill Climb (Strictly Increasing)
        for i in range(0, peak_idx):
            if arr[i] >= arr[i + 1]:  # Must strictly increase
                return False
                
        # 2. Check Downhill Descent (Strictly Decreasing)
        for i in range(peak_idx, len(arr) - 1):
            if arr[i] <= arr[i + 1]:  # Must strictly decrease
                return False
                
        return True
