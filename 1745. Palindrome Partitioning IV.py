"""
Method 1:
Brute-Force

Time complexity: O(N**2)
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


if __name__ == "__main__":
    sol = Solution()
    s = "bbab"
    result = sol.checkPartitioning(s)
    print(result)
