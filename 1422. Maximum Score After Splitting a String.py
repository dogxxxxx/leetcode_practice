"""
Method 1:
Loop through s to get total ones
Then loop through s again to find the answer

Time complexity: O(N)
Space complexity: O(1)
"""

class Solution:
    def maxScore(self, s: str) -> int:
        zeros = 0
        result = 0
        total_ones = 0
        for i in s:
            if i == '1':
                total_ones += 1
        for i in range(len(s) - 1):
            if s[i] == '0':
                zeros += 1
            else:
                total_ones -= 1
            result = max(result, total_ones + zeros)
        return result
    
"""
Method 2:
Math

Time complexity: O(N)
Space complexity: O(1)
"""

class Solution:
    def maxScore(self, s: str) -> int:
        zeros = 0
        ones = 0
        result = -1
        for i in range(len(s) - 1):
            if s[i] == '0':
                zeros += 1
            else:
                ones += 1
            result = max(result, zeros - ones)
        result += ones
        if s[-1] == '1':
            result += 1
        return result


if __name__ == "__main__":
    s = "1111"
    result = Solution().maxScore(s)
    print(result)