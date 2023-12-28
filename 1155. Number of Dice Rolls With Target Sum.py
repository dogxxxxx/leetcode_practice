"""
Method 1:

"""

class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        dp = [[-1 for _ in range(target + 1)] for _ in range(n + 1)]
        mod = 10 ** 9 + 7
        def get_nums(dp, n, k, target):
            if n == 0 and target == 0:
                return 1
            elif n == 0 or target < 0:
                return 0
            if dp[n][target] != -1:
                return dp[n][target]
            
            result = 0
            for i in range(1, k + 1):
                result += get_nums(dp, n - 1, k, target - i)
                result %= mod
            dp[n][target] = result
            return dp[n][target]
        
        result = get_nums(dp, n, k, target)
        return result % mod
        
            
if __name__ == "__main__":
    n = 2
    k = 12
    target = 8
    result = Solution().numRollsToTarget(n, k, target)
    print(result)