from typing import List
from collections import deque
"""
Method 1:
Get the indices of zeros. Then loop through nums from the begining.
The upperbound of i is the index of zeros.
If the step length is larger than the current upper bound,
the current upper bound will be larger until no zeros.

Time complexity: O(N)
Space complexity: O(N)
"""

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        zeros = []
        for i in range(len(nums)):
            if nums[i] == 0:
                zeros.append(i)
        if len(zeros) == 0:
            return True
        i = 0
        j = 0
        target = len(nums) - 1
        while i < target:
            i_upper = zeros[j]
            if i == i_upper:
                return False
            while i + nums[i] > zeros[j]:
                j += 1
                if j == len(zeros):
                    return True
            i += 1
        return True
    
"""
Method 2:
Use queue to store the steps to go and set some limit to return True.

Time complexity: O(N**2)
Space complexity: O(N)
"""

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        queue = deque([i + 1 for i in range(nums[0])])
        i = 1
        while queue:
            num = nums[queue[0]]
            if num + i > len(nums):
                return True

            if num + i > queue[-1]:
                for x in range(queue[-1], num + i):
                    queue.append(x + 1)
            queue.popleft()
            i += 1
            if i >= len(nums):
                return True
            
        return False


if __name__ == "__main__":
    sol = Solution()
    nums = [3,3,1,0,0,4]
    result = sol.canJump(nums)
    print(result)
