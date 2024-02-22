from typing import List
"""
Method 1:
Create an array representing each person. Iterate through trust.
If a person trust anyone, assign him to -1 since he is not the 
potential judge. Iterate through the array, if anyone gets n-1
trusts, he is the judge, else, no judge.

Time complexity: O(N)
Space complexity: O(N)
"""
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        arr = [0] * n
        for (a, b) in trust:
            arr[a - 1] = -1
            arr[b - 1] += 1
        for i in range(len(arr)):
            if arr[i] == n - 1:
                return i + 1
        return -1
    
    
if __name__ == "__main__":
    n = 3
    trust = [[1,3],[2,3],[3,1]]
    result = Solution().findJudge(n, trust)
    print(result)
