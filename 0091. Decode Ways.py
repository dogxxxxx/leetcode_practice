"""
Method 1:
Create a dp with length = len(s) + 1
to deal with i - 2

Time complexity: O(N)
Space complexity: O(N)
"""

class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == "0":
            return 0
        dp = [0] * (len(s)+1)
        dp[0] = 1
        dp[-1] = 1
        for i in range(1, len(s)):
            if s[i] != "0":
                dp[i] += dp[i - 1]
            if 10 <= int(s[i-1:i+1]) <= 26:
                dp[i] += dp[i - 2]  
        return dp[-2]
    

if __name__ == "__main__":
    s = "1"
    result = Solution().numDecodings(s)
    print(result)