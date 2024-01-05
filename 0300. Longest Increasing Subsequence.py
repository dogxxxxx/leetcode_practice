from typing import List
"""
Method 1:
Calculate maximum length from the end

Time complexity: O(Nlog(N))
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
    nums = [10,9,2,5,3,7,101,18]
    result = Solution().lengthOfLIS(nums)
    print(result)