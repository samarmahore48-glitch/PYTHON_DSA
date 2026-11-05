class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        res=[]
        for i in range(0,len(intervals)):
            if intervals[i][0]>newInterval[0]:
                intervals.insert(i,newInterval)
                break
        else:
            intervals.append(newInterval)
        res=[]
        res.append(intervals[0])
        for i in range(1,len(intervals)):
            if res[-1][1]>=intervals[i][0]:
                res[-1][1]=max(res[-1][1],intervals[i][1])
            else:
                res.append(intervals[i])
        return res
