from typing import List
"""
Method 1:
Iterate 2 times, one from the begining and the other from the end.
Modify the candies given to meet the requirement

Time complexity: O(N)
Space complexity: O(N)
"""

class Solution:
    def candy(self, ratings: List[int]) -> int:
        candies = [1] * len(ratings)
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i - 1] and candies[i] <= candies[i - 1]:
                candies[i] = candies[i - 1] + 1
        for i in range(len(ratings) - 2, -1, -1):
            if ratings[i] > ratings[i + 1] and candies[i] <= candies[i + 1]:
                candies[i] = candies[i + 1] + 1
        return sum(candies)
    

if __name__ == "__main__":
   ratings = [1,2,2]
   result = Solution().candy(ratings)
   print(result)
