"""
Method 1:
Brute-Force

Time complexity: O(N**3)
Space complexity: O(N)
"""

class Solution:
    def checkPartitioning(self, s: str) -> bool:
        def is_palindrome(s: str):
            if s == s[::-1] or len(s) == 1:
                return True
            else:
                return False
        
        first_inds = []
        for i in range(1, len(s)):
            if is_palindrome(s[0:i]):
                first_inds.append(i)
        for ind in first_inds:
            for i in range(ind + 1, len(s)):
                if is_palindrome(s[ind:i]) and is_palindrome(s[i:]):
                    return True
        return False
    
"""
Method 2:
DP

Time complexity: O(N**2)
Space complexity: O(N**2)
"""

class Solution:
    def checkPartitioning(self, s: str) -> bool:
        dp = {}
        for i in range(len(s) - 1, -1, -1):
            dp[i] = {}
            for j in range(i, len(s)):
                if (s[i] == s[j]) and (j - i < 2 or j-1 in dp[i+1]):
                    dp[i][j] = True
        
        for ind1 in range(1, len(s) - 1):
            if ind1 - 1 in dp[0]:
                for ind2 in range(ind1, len(s) - 1):
                    if ind2 in dp[ind1] and (len(s) - 1 in dp[ind2 + 1]):
                        return True
        return False



if __name__ == "__main__":
    sol = Solution()
    s = "abcbdd"
    result = sol.checkPartitioning(s)
    print(result)
