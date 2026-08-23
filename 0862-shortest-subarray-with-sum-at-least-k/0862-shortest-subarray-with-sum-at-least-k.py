class Solution:
    def shortestSubarray(self, nums, k):
        prefix = [0]

        for x in nums:
            prefix.append(prefix[-1] + x)

        q = []
        ans = len(nums) + 1

        for i in range(len(prefix)):

            while q and prefix[i] - prefix[q[0]] >= k:
                ans = min(ans, i - q[0])
                q.pop(0)

            while q and prefix[i] <= prefix[q[-1]]:
                q.pop()

            q.append(i)

        return -1 if ans == len(nums) + 1 else ans