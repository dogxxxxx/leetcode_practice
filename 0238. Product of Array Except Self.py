from typing import List
"""
Method 1:
Brute Force
Determine the nums of 0 first.
If nums of 0 is bigger than 1, all the elements in the list is 0.
If nums of 0 equals to 1, all the elements in the list except for 0 itself are 0.
If nums of 0 equals to 0, all the elements in the list is the product divided by itself.

Time complexity: O(N)
Space complexity: O(1) (only store product and zeros_num. The result is not included)
"""

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        zeros_num = 0
        for num in nums:
            if num == 0:
                zeros_num += 1
                continue
            product *= num

        result = []
        if zeros_num >= 2:
            result = [0]*len(nums)
        elif zeros_num == 1:
            for num in nums:
                if num == 0:
                    result.append(product)
                else:
                    result.append(0)
        else:
            for num in nums:
                result.append(int(product / num))

        return result

"""
Method 2:
Iterate through the nums and calculate the product of previous
numbers and post numbers.

Time complexity: O(N)
Space complexity: O(1)
Date: 2024/03/14
"""

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [1] * n
        prev = 1
        post = 1
        for i in range(n):
            result[i] *= prev
            prev *= nums[i]
            result[n - i - 1] *= post
            post *= nums[n - i - 1]
        return result
    

if __name__ == "__main__":
    nums = [1,2,3,4]
    result = Solution().productExceptSelf(nums)
    print(result)