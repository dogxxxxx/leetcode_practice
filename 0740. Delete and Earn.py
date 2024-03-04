from typing import List
"""
Method 1:
Create a list to store the frequency of each number.
Then, iterate through the frequency list. Use prev and
curr to simulate the situation.

Time complexity: O(N)
Space complexity: O(N)
"""

class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        freq = [0] * (max(nums) + 1)
        for num in nums:
            freq[num] += 1
        prev = 0
        curr = freq[0] * 0
        for i in range(1, len(freq)):
            tmp = curr
            curr = max(prev + i * freq[i], curr)
            prev = tmp
        return curr


if __name__ == "__main__":
    nums = [4,2,3]
    result = Solution().deleteAndEarn(nums)
    print(result)