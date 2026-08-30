class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n = len(nums)

        mini = 0
        maxi = 0

        for i in range(1, n):
            if nums[i] < nums[mini]:
                mini = i

            if nums[i] > nums[maxi]:
                maxi = i

        left = min(mini, maxi)
        right = max(mini, maxi)

        # Case 1: Delete everything from left
        option1 = right + 1

        # Case 2: Delete everything from right
        option2 = n - left

        # Case 3: Delete one from left and one from right
        option3 = (left + 1) + (n - right)

        return min(option1, option2, option3)