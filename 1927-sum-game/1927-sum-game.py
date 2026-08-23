class Solution:
    def sumGame(self, num: str) -> bool:
        n = len(num)
        half = n // 2

        left_sum = right_sum = 0
        left_q = right_q = 0

        for i in range(half):
            if num[i] == '?':
                left_q += 1
            else:
                left_sum += int(num[i])

        for i in range(half, n):
            if num[i] == '?':
                right_q += 1
            else:
                right_sum += int(num[i])

        diff = left_sum - right_sum
        q_diff = left_q - right_q

        # Unequal number of ? with odd difference:
        # Alice can always force a win.
        if abs(q_diff) % 2 == 1:
            return True

        # Equal number of ? -> only existing difference matters
        if q_diff == 0:
            return diff != 0

        # Even difference in ?s
        if q_diff > 0:
            return diff + 9 * (q_diff // 2) != 0
        else:
            return diff - 9 * ((-q_diff) // 2) != 0