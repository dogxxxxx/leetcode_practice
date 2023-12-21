from typing import List
"""
Method 1:
Create a dictionary to store the interval and the corresponding index.
Then, sort the intervals by the first element to perform binary search.

Time complexity: O(Nlog(N))
Space complexity: O(N)
"""

class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        interval2id = dict()
        result = [-1] * len(intervals)
        for i in range(len(intervals)):
            interval2id[intervals[i][0]] = i
        intervals = sorted(intervals, key=lambda x: x[0])

        for interval in intervals:
            low = 0
            high = len(intervals) - 1
            right = interval[1]
            while low <= high:
                mid = low + (high - low) // 2
                if right == intervals[mid][0]:
                    result[interval2id[interval[0]]] = interval2id[intervals[mid][0]]
                    break
                elif right > intervals[mid][0]:
                    low = mid + 1
                else:
                    high = mid - 1
                    result[interval2id[interval[0]]] = interval2id[intervals[mid][0]]
        return result


if __name__ == "__main__":
    intervals = [[4,5],[2,3],[1,2]]
    result = Solution().findRightInterval(intervals)
    print(result)