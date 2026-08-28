class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        n = len(s)

        # Count characters
        cnt = [0] * 26
        for ch in s:
            cnt[ord(ch) - ord('a')] += 1

        # A palindrome can have at most one odd frequency
        if sum(x % 2 for x in cnt) > 1:
            return ""

        # Middle character for odd length
        middle = ""
        if n % 2:
            for i in range(26):
                if cnt[i] % 2:
                    middle = chr(ord('a') + i)
                    break

        # Characters available for the left half
        half_cnt = [x // 2 for x in cnt]
        m = n // 2

        # --------------------------------------------------
        # Find how much of target's left half we can match
        # --------------------------------------------------
        rem = half_cnt[:]
        matched = 0

        while matched < m:
            c = ord(target[matched]) - ord('a')

            if rem[c] == 0:
                break

            rem[c] -= 1
            matched += 1

        # --------------------------------------------------
        # Case 1:
        # We can make the entire left half equal to target's
        # left half.
        # --------------------------------------------------
        if matched == m:
            left = target[:m]

            candidate = left + middle + left[::-1]

            if candidate > target:
                return candidate

        # --------------------------------------------------
        # Case 2:
        # Make the left half greater at some position.
        #
        # Try the rightmost possible position first because
        # that gives the smallest lexicographic answer.
        # --------------------------------------------------
        start = min(matched, m - 1)

        for i in range(start, -1, -1):

            # Rebuild remaining character counts after
            # using target[:i]
            rem = half_cnt[:]

            valid = True

            for j in range(i):
                c = ord(target[j]) - ord('a')

                if rem[c] == 0:
                    valid = False
                    break

                rem[c] -= 1

            if not valid:
                continue

            # At position i, choose the smallest character
            # strictly greater than target[i].
            target_c = ord(target[i]) - ord('a')

            for c in range(target_c + 1, 26):

                if rem[c] == 0:
                    continue

                # Use this larger character
                rem[c] -= 1

                # Fill everything after it with smallest chars
                suffix = ""

                for x in range(26):
                    suffix += chr(ord('a') + x) * rem[x]

                left = target[:i] + chr(ord('a') + c) + suffix

                candidate = left + middle + left[::-1]

                if candidate > target:
                    return candidate

                # Restore
                rem[c] += 1

        return ""