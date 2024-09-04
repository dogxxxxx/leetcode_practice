from typing import List
"""
Method 1:
Create a list to store if the nums[i] is larger than
any number with index < i by iterating the nums from the left.
Then, iterate from the right to check another requirement of beauty = 2
and check the requirement of beauty = 1 at the same time.

Time complexity: O(N)
Space complexity: O(N)
"""

class Solution:
    def sumOfBeauties(self, nums: List[int]) -> int:
        right_ok = [False] * len(nums)
        left_max = nums[0]
        res = 0

        for i in range(1, len(nums) - 1):
            if nums[i] > left_max:
                left_max = nums[i]
                right_ok[i] = True
        
        right_min = nums[-1]
        for i in range(len(nums) - 2, 0, -1):
            if nums[i] < right_min and right_ok[i]:
                res += 2
            elif nums[i] < nums[i + 1] and nums[i] > nums[i - 1]:
                res += 1
            
            if nums[i] < right_min:
                right_min = nums[i]
        return res


if __name__ == "__main__":
    nums = [1,2,3,4,5,7,8,9,10]
    res = Solution().sumOfBeauties(nums)
    print(res)
    