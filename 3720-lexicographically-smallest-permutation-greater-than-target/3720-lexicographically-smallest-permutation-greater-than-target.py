class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:

        count = [0] * 26

        # Count characters of s
        for ch in s:
            count[ord(ch) - ord('a')] += 1

        n = len(target)

        # We will try to match target from left to right
        prefix = []

        for i in range(n):

            t = ord(target[i]) - ord('a')

            # If target[i] is available, keep it
            if count[t] > 0:
                count[t] -= 1
                prefix.append(target[i])

            else:
                break

        # If we matched the complete target,
        # we still need a permutation strictly greater than it.
        if len(prefix) == n:

            # Backtrack from right
            for i in range(n - 1, -1, -1):

                # Put target[i] back
                t = ord(target[i]) - ord('a')
                count[t] += 1
                prefix.pop()

                # Find smallest character > target[i]
                for x in range(t + 1, 26):

                    if count[x] > 0:

                        count[x] -= 1

                        ans = prefix + [chr(x + ord('a'))]

                        # Fill remaining characters smallest first
                        for c in range(26):
                            ans += [chr(c + ord('a'))] * count[c]

                        return ''.join(ans)

            return ""

        # We failed to match target at position len(prefix)
        i = len(prefix)
        t = ord(target[i]) - ord('a')

        # Try a character greater than target[i]
        for x in range(t + 1, 26):

            if count[x] > 0:

                count[x] -= 1

                ans = prefix + [chr(x + ord('a'))]

                # Fill remaining characters
                for c in range(26):
                    ans += [chr(c + ord('a'))] * count[c]

                return ''.join(ans)

        # If we cannot make current position greater,
        # backtrack to an earlier position.
        for i in range(len(prefix) - 1, -1, -1):

            # Restore the character at this position
            old = ord(prefix.pop()) - ord('a')
            count[old] += 1

            current = ord(target[i]) - ord('a')

            # Find smallest character greater than target[i]
            for x in range(current + 1, 26):

                if count[x] > 0:

                    count[x] -= 1

                    ans = prefix + [chr(x + ord('a'))]

                    for c in range(26):
                        ans += [chr(c + ord('a'))] * count[c]

                    return ''.join(ans)

        return ""