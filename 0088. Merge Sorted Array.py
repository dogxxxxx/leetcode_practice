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
Simpl2 while loop.

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
