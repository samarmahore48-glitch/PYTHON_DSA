class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2:
            return 0

        is_prime = [True] * (n + 1)
        is_prime[0] = is_prime[1] = False

        p = 2
    # Check primes up to p * p <= n
        while p * p <= n:
            if is_prime[p]:
            # Mark multiples starting at p * p
                i = p * p
                while i <= n:
                    is_prime[i] = False
                    i += p
            p += 1

        return sum(is_prime)


# Example Usage:
