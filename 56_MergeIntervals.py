# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

    def __repr__(self):
        return str([self.start, self.end])

class Solution:
    def parse(self, intervals):
        result = []
        for interval in intervals:
            result.append(Interval(interval[0], interval[1]))
        return self.merge(result)

    # @param {Interval[]} intervals
    # @return {Interval[]}
    def merge(self, intervals):
        result = []
        for inter in sorted(intervals, key=lambda x: x.start):
            if result and inter.start <= result[-1].end:
                result[-1].end = max(inter.end, result[-1].end)
            else:
                result.append(inter)
        return result

    def bmerge(self, intervals):
        intervals = sorted(intervals[:], key=lambda inter: inter.start)
        idx = 0
        while True:
            if idx > (len(intervals) - 2):
                break
            intera, interb = intervals[idx], intervals[idx+1]
            if intera.start > interb.end or intera.end < interb.start:
                idx += 1
            else:
                start = intera.start
                if intera.start > interb.start:
                    start = interb.start
                end = intera.end
                if intera.end < interb.end:
                    end = interb.end
                del intervals[idx:idx+2]
                intervals.insert(idx, Interval(start, end))
        return intervals

            
    def amerge(self, intervals):
        result = sorted(intervals[:], key=lambda inter: inter.start)
        while True:
            tmp = result[:]
            intera, interb = self.hasOverlap(tmp)
            if intera == None and interb == None:
                break
            else:
                idx = min(tmp.index(intera), tmp.index(interb))
                tmp.remove(intera)
                tmp.remove(interb)
                start = intera.start
                if intera.start > interb.start:
                    start = interb.start
                end = intera.end
                if intera.end < interb.end:
                    end = interb.end
                tmp.insert(idx, Interval(start, end))
            result = tmp
        return result

    def hasOverlap(self, intervals):
        tmp = intervals[:]
        while tmp:
            target = tmp.pop()
            for interval in tmp:
                # no crossing
                if interval.start > target.end or interval.end < target.start:
                    continue
                else:
                    return target, interval
        return None, None

                
if __name__ == "__main__":
    sol = Solution()
    print sol.parse([[1,3],[2,6],[8,10],[15,18]]) 
    print sol.parse([[1,4],[1,4]]) 
