# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

    def __repr__(self):
        return str([self.start, self.end])

class Solution:
    def parse(self, intervals, newInterval):
        result = []
        for interval in intervals:
            result.append(Interval(interval[0], interval[1]))
        return self.insert(result, Interval(newInterval[0], newInterval[1]))

    # @param {Interval[]} intervals
    # @param {Interval} newInterval
    # @return {Interval[]}
    def insert(self, intervals, newInterval):
        start = newInterval.start
        end = newInterval.end
        left = 0
        right = 0
        while right < len(intervals):
            if start <= intervals[right].end:
                if end < intervals[right].start:
                    break
                start = min(intervals[right].start, start)
                end   = max(intervals[right].end  ,   end)
            else:
                left += 1
            right += 1
        return intervals[:left] + [Interval(start, end)] + intervals[right:]

    def ainsert(self, intervals, newInterval):
        if not intervals:
            return [newInterval]
        result = [newInterval]
        for inter in intervals:
            if inter.end < result[-1].start:
                result.insert(-1, inter)
            elif inter.start <= result[-1].end:
                result[-1].start = min(inter.start, result[-1].start)
                result[-1].end = max(inter.end, result[-1].end)
            else:
                result.append(inter)
        return result

 
if __name__ == "__main__":
    sol = Solution()
    print sol.parse([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,9]) 
    print sol.parse([[1,5]], [2,7]) 
