from typing import List
from functools import cache
"""
Method 1:

"""

class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        length = len(jobDifficulty)
        maximum = sum(jobDifficulty)
        if length < d:
            return -1
        
        @cache
        def recur(start, days):
            if start == length - 1 or days == 1:
                return max(jobDifficulty[start:])
            
            result = maximum
            for i in range(start + 1, length - days + 2):
                job_cur = max(jobDifficulty[start:i]) + recur(i, days - 1)
                result = min(job_cur, result)
            return result
        return recur(0, d)
    

if __name__ == "__main__":
    jobDifficulty = [380,302,102,681,863,676,243,671,651,612,162,561,394,856,601,30,6,257,921,405,716,126,158,476,889,699,668,930,139,164,641,801,480,756,797,915,275,709,161,358,461,938,914,557,121,964,315]
    d = 10
    result = Solution().minDifficulty(jobDifficulty, d)
    print(result)
