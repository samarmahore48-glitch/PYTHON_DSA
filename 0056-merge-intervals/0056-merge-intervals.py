class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        if len(intervals) <= 1:
            return intervals

        intervals.sort(key=lambda x: x[0])

        i = 1

        while i < len(intervals):
            if intervals[i-1] != 0 and intervals[i] != 0:
                if intervals[i-1][1] >= intervals[i][0]:

                    a = [
                        min(intervals[i-1][0], intervals[i][0]),
                        max(intervals[i-1][1], intervals[i][1])
                    ]

                    intervals[i] = a
                    intervals[i-1] = 0

            i += 1

        res = list(filter(lambda x: x != 0, intervals))
        return res