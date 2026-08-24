class Solution:
    def stoneGameVIII(self, stones: List[int]) -> int:

        n = len(stones)

        # prefix sum
        prefix = [0] * n
        prefix[0] = stones[0]

        for i in range(1, n):
            prefix[i] = prefix[i - 1] + stones[i]

        # Alice must eventually choose a prefix of at least 2 stones.
        # Start with the only possible choice when 2 stones remain.
        ans = prefix[n - 1]

        for i in range(n - 2, 0, -1):
            ans = max(ans, prefix[i] - ans)

        return ans        