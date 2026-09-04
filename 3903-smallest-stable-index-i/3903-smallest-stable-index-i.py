class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        fi = [nums[0]]

        for i in range(len(nums)):
            fi.append(nums[i]) if i > 0 else None

            la = nums[i:]

            if max(fi) - min(la) <= k:
                return i

        return -1