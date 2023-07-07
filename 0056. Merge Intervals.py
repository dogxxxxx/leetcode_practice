"""
Method 1:
Sort the intervals first and then check if the intervals need to be combined.

Time complexity:
Space complexity: O(1)
"""

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        def combine(lst1, lst2):
            return [min(lst1[0], lst2[0]), max(lst1[1], lst2[1])]
        
        intervals = sorted(intervals, key=lambda x: x[0])
        i = 0
        while i < len(intervals)-1:
            if not intervals[i+1][0] > intervals[i][1]:
                newInterval = combine(intervals[i], intervals[i+1])
                intervals[i] = newInterval
                intervals.pop(i+1)
            else:
                i += 1
        return intervals
