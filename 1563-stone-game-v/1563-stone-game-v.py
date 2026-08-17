from functools import cache
from itertools import accumulate

class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        n = len(stoneValue)
        pre = list(accumulate(stoneValue, initial=0))

        @cache
        def dfs(l, r):
            if l >= r:
                return 0

            ans = 0
            left = 0
            right = pre[r + 1] - pre[l]

            for k in range(l, r):
                left += stoneValue[k]
                right -= stoneValue[k]

                if left < right:
                    if ans >= 2 * left:
                        continue
                    ans = max(ans, left + dfs(l, k))

                elif left > right:
                    if ans >= 2 * right:
                        break
                    ans = max(ans, right + dfs(k + 1, r))

                else:
                    ans = max(
                        ans,
                        left + dfs(l, k),
                        right + dfs(k + 1, r)
                    )

            return ans

        return dfs(0, n - 1)