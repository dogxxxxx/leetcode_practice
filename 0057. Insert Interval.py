"""
Method 1:
Create a list to store intervals that is smaller than new interval.
When intervals begin to overlap with new interval, change the start and end points of the new interval.
After overlapping, return the list + new interval + remaining intervals.

### Modify intervals in-place can reduce space complexity to O(1)

Time complexity: O(N)
Space complexity: O(N)
"""

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        s, e = newInterval

        for i in range(len(intervals)):
            if intervals[i][1] < s:
                result.append(intervals[i])
            elif intervals[i][0] > e:
                return result + [[s, e]] + intervals[i:]
            else:
                s = min(intervals[i][0], s)
                e = max(intervals[i][1], e)
                
        result.append([s, e])
        return result
