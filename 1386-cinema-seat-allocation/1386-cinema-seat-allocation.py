class Solution:
    def maxNumberOfFamilies(self, n, reservedSeats):
        rows = {}

        # Store reserved seats row-wise
        for row, seat in reservedSeats:
            if row not in rows:
                rows[row] = set()
            rows[row].add(seat)

        # Every completely empty row can fit 2 families
        ans = (n - len(rows)) * 2

        # Check only rows that have reservations
        for reserved in rows.values():

            left = all(seat not in reserved for seat in [2, 3, 4, 5])
            middle = all(seat not in reserved for seat in [4, 5, 6, 7])
            right = all(seat not in reserved for seat in [6, 7, 8, 9])

            if left and right:
                ans += 2

            elif left or middle or right:
                ans += 1

        return ans