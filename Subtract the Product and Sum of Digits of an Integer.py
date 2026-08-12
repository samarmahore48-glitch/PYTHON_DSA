class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        su = 0
        pr = 1

        while n > 0:
            digit = n % 10

            su += digit
            pr *= digit

            n //= 10

        return pr - su