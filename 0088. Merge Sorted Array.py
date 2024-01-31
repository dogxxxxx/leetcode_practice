from typing import List
"""
Method 1:
Recursive algorithm. Compare 2 numbers until nums2 list is all inserted into nums1 list.
Or nums1 and nums2 can be declared as global before merge function and then there's no need
to pass nums1 and nums2 into recursive function.

Time complexity: O(m+n)
Space complexity: O(M+n), M is the length of nums1
"""

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        def recursive(nums1, nums2, m, n):
            if n-1 < 0:
                return
            elif m-1 < 0:
                nums1.insert(m, nums2[n-1])
                nums1.pop()
                recursive(nums1, nums2, m, n-1)
            elif nums1[m-1] <= nums2[n-1]:
                nums1.insert(m, nums2[n-1])
                nums1.pop()
                recursive(nums1, nums2, m, n-1)
            else:
                recursive(nums1, nums2, m-1, n)
            
        recursive(nums1, nums2, m, n)

"""
Method 2:
Simple while loop.

Time complexity: O(m+n)
Space complexity: O(M+n), M is the length of nums1
"""

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        while n-1 >= 0:
            if m-1 < 0:
                nums1.insert(m, nums2[n-1])
                nums1.pop()
                n = n - 1
            elif nums1[m-1] <= nums2[n-1]:
                nums1.insert(m, nums2[n-1])
                nums1.pop()
                n = n - 1
            else:
                m = m - 1

"""
Review 1:
Add elements from the end
until pointer 2 points to 0.

Time complexity: O(m + n)
Space complexity: O(1)
"""

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        index = m + n - 1
        for i in range(n - 1, -1, -1):
            while m - 1 >= 0 and nums2[i] <= nums1[m - 1]:
                nums1[index] = nums1[m - 1]
                m -= 1
                index -= 1
            nums1[index] = nums2[i]
            index -= 1


if __name__ == "__main__":
    nums1 = [2,0]
    nums2 = [1]
    n = 1
    m = 1
    Solution().merge(nums1, m, nums2, n)
    print(nums1)