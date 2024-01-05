from typing import List
"""
Method 1:
Calculate maximum length from the end

Time complexity: O(N^2)
Space complexity: O(N)
"""

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        dp[-1] = 1
        for i in range(len(nums) - 2, -1, -1):
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    dp[i] = max(dp[i], dp[j])
            dp[i] += 1
        return max(dp)
    

if __name__ == "__main__":
    nums = [4,10,4,3,8,9]
    result = Solution().lengthOfLIS(nums)
    print(result)