from typing import List
"""
Method 1:
Create a list to store the missing elements
while rotating

Time complexity: O(N)
Space complexity: O(N)
"""

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        tmp = nums[-k:]
        for i in range(len(nums) - 1, k - 1, -1):
            nums[i] = nums[i - k]
        for i in range(k):
            nums[i] = tmp[i]

"""
Method 2:
Append the nums to simulate the rotation

Time complexity: O(k)
Space complexity: O(k)
"""

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        k = k % length
        for i in range(length - k):
            nums.append(nums[i])
        del nums[:length - k]

"""
Method 3:
Math

Time complexity: O(N)
Space complexity: O(1)
"""

class Solution:
    def reverse(self, nums, start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        self.reverse(nums, 0, len(nums) - 1)
        self.reverse(nums, 0, k - 1)
        self.reverse(nums, k, len(nums) - 1)

if __name__ == "__main__":
    nums = [1,2,3,4,5,6,7]
    k = 3
    Solution().rotate(nums, k)
    print(nums)
