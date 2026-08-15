class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        if not timeSeries:
            return 0
        tot = 0
        for i in range(len(timeSeries) - 1):
            gap = timeSeries[i+1] - timeSeries[i]
            tot += min(gap, duration)
        
        tot += duration
        return tot