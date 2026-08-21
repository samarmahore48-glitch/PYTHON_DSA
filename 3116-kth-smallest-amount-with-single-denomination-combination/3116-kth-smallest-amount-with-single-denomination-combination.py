from math import lcm
from itertools import combinations
from typing import List

class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        # Helper function to count unique coin multiples <= target
        def count_multiples(target: int) -> int:
            total = 0
            n = len(coins)
            
            # Iterate through all non-empty subsets of coins
            # Using bitmasking (1 to 2^n - 1) to find subsets
            for i in range(1, 1 << n):
                current_lcm = 1
                bits_count = 0
                
                for j in range(n):
                    if (i >> j) & 1:
                        current_lcm = lcm(current_lcm, coins[j])
                        bits_count += 1
                
                # Inclusion-Exclusion formula
                if bits_count % 2 == 1:
                    total += target // current_lcm
                else:
                    total -= target // current_lcm
                    
            return total

        # Binary search range boundaries
        low = 1
        high = min(coins) * k
        ans = high
        
        while low <= high:
            mid = (low + high) // 2
            if count_multiples(mid) >= k:
                ans = mid
                high = mid - 1  # Try to find a smaller valid amount
            else:
                low = mid + 1   # Increase the amount
                
        return ans
